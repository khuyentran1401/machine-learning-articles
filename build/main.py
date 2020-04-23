#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser
import os, sys
from pathlib import Path
import time
import requests

# Machine Learning Articles
URL_REPO_ISSUES = 'https://api.github.com/repos/khuyentran1401/machine-learning-articles/issues'

def get_issues(url_issues):
  """Get Issues per page. No Pull Request"""


  def get_resource(url_issue):
    """Get Issues List if not Error"""
    response = requests.get(url_issue)
    issues_json = response.json()

    if isinstance(issues_json, list):
      issues = [issue for issue in issues_json
                if issue.get('pull_request') is None]
    else:
      issues = []
    
    return issues, response.links.get('next')


  issues, _next = get_resource(url_issues)

  while _next:
    time.sleep(1)
    url_issues = _next.get('url')
    temp, _next = get_resource(url_issues)
    issues.extend(temp)

  return issues


def create_issue(issue, repository, token):
  """Create Owner Issue using API REST GitHub v3"""

  headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
  response = requests.post(repository, json=issue, headers=headers)

  return response.status_code == 201


def main(token, repository):
  """Entry point main"""

  if not token:
    sys.exit('You need set the secrets.PAT')

  if not repository:
    sys.exit('You need set the GITHUB_REPOSITORY')

  URL_OWNER_ISSUES = f'https://api.github.com/repos/{repository}/issues'  
  issues = get_issues(URL_REPO_ISSUES)  
  issues_owner = get_issues(URL_OWNER_ISSUES)
  issues_owner_title = [issue.get('title') for issue in issues_owner] 

  dir_issues = Path('build/issues')
  issues_files = []

  if not dir_issues.is_dir():
      dir_issues.mkdir()
  else:
      issues_files= [int(file.stem.split('_')[1])
                    for file in Path().glob(f'{dir_issues}/issue_*.md')]

  # Create issues .md in dir_issues
  for issue in issues:
      number = issue.get('number')
      has_title = issue.get('title') in issues_owner_title
      # Issues number Origin is diferent in Fork. Check by title
      if not has_title:
        file_name = f'issue_{number}'
        title = issue.get('title')
        body = issue.get('body')
        labels = issue.get('labels')
        issue = {'title': title, 'body': body, 'labels': labels}

        time.sleep(1)
        if create_issue(issue, URL_OWNER_ISSUES, token):
          with open(f'{dir_issues}/{file_name}.md', 'w') as file_md:
              file_md.write(body)
        else:
          sys.exit('Error Create Issue!!!')

if __name__ == "__main__":
  parser = ArgumentParser(
    description='Create Issues from khuyentran1401/machine-learning-articles'
  )

  parser.add_argument(
    '-t',
    '--token',
    metavar='GH_TOKEN',
    type=str,
    nargs='?',
    default=os.getenv('GH_TOKEN'),
    help='Personal Access Token for create Issues'
  )

  parser.add_argument(
    '-r',
    '--repo',
    metavar='GH_REPOSITORY',
    type=str,
    nargs='?',
    default=os.getenv('GH_REPOSITORY'),
    help='GitHub Owner Repository'
  )

  args = parser.parse_args()
  token = args.token
  repository = args.repo
  
  main(token, repository)
