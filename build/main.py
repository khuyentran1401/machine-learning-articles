#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser
import os
import sys
from pathlib import Path
from string import Template
import time
from urllib.parse import quote_plus
from typing import Optional, List, Dict, Tuple, Any
import requests

ISSUE = Optional[Dict[str, Any]]
IssuesListOpt = Optional[List[ISSUE]]
# Machine Learning Articles
URL_REPO_ISSUES = 'https://api.github.com/repos/khuyentran1401/machine-learning-articles/issues'


def get_issues(url_issues: str) -> IssuesListOpt:
    """Get Issues per page. No Pull Request"""

    def get_resource(url_issue: str) -> Tuple[IssuesListOpt, Dict[str, str]]:
        """Get Issues List if not Error"""
        response = requests.get(url_issue)
        issues_json = response.json()

        if isinstance(issues_json, list):
            _issues = [issue for issue in issues_json
                       if issue.get('pull_request') is None]
        else:
            _issues = []

        return _issues, response.links.get('next')

    issues, _next = get_resource(url_issues)

    while _next:
        time.sleep(1)
        url_issues = _next.get('url')
        temp, _next = get_resource(url_issues)
        issues.extend(temp)

    return issues


def create_issue(issue: ISSUE, repository: str, token: str) -> int:
    """Create Owner Issue using API REST GitHub v3"""

    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    response = requests.post(repository, json=issue, headers=headers)

    return response.status_code == 201


def export_issues_html(issues=get_issues(URL_REPO_ISSUES)) -> None:
    """Create index.html from API Issues URL"""
    # import json

    url_repository = URL_REPO_ISSUES.rsplit('/', 1)[-2]

    if len(issues) > 0:
        url_repository = issues[0].get('repository_url')

    def get_label_template(label: Optional[Dict[str, Any]]) -> str:
        """Label template HTML"""
        url_split = url_repository.split('/', 4)
        label_name = ""

        if label is not None:
            label_name = label.get('name')

        if " " in label_name:
            quote_label = quote_plus(f'"{label_name}"')
        else:
            quote_label = quote_plus(f'{label_name}')

        url_issue = (f"https://github.com/{url_split[-1]}/issues/"
                     f"?q=is%3Aissue+is%3Aopen+label%3A{quote_label}")

        return (f"""<span class="labels lh-default d-block d-md-inline">"""
                f"""<a class="d-inline-block IssueLabel" style="background-color: #{label.get('color')}; """
                f"""color: #000000" href="{url_issue}" title="{label_name}">{label_name}</a></span>""")

    def get_author_template(user: Dict[str, Any]) -> str:
        """Author template HTML"""
        return (f"""<a title="Create by {user.get('login')}" href="https://github.com/{user.get('login')}">"""
                f"""<img class="avatar avatar-user" src="{user.get('avatar_url')}" width="20" height="20" """
                f"""alt="@{user.get('login')}">{user.get('login')}</a>""")

    def get_title_template(_issue: Dict[str, Any]) -> str:
        """Issue Title template HTML"""
        return f"""<a href="{_issue.get('html_url')}">{_issue.get('title')}</a>"""

    # with open('build/issues.json', 'r') as file:
    #   issues = json.load(file)

    with open('build/index.tpl', 'r') as file:
        tpl = file.read()

    index_template = Template(tpl)

    rows_issues = ""
    gh_repository = os.getenv('GH_REPOSITORY')

    if gh_repository:
        gh_repository = gh_repository.split('/')[-1]
    else:
        gh_repository = 'machine-learning-articles'

    gh_repository_description = os.getenv('GH_REPOSITORY_DESCRIPTION')

    if not gh_repository_description:
        gh_repository_description = ("List of interesting articles on different topics"
                                     " of machine learning and deep learning")

    for issue in issues:
        title = get_title_template(issue)
        labels = " ".join([get_label_template(label) for label in issue.get('labels')])
        author = get_author_template(issue.get('user'))
        rows_issues += f"<tr><td>{title}</td><td>{labels}</td><td>{author}</td></tr>\n\t\t\t\t"

    with open('index.html', 'w') as file:
        file.write(index_template.substitute(GH_REPOSITORY_DESCRIPTION=gh_repository_description,
                                             GH_REPOSITORY=gh_repository,
                                             ROWS_ISSUES=rows_issues))


def main(token: str, repository: str) -> None:
    """Entry point main"""

    if not token:
        sys.exit('You need set the secrets.PAT')

    if not repository:
        sys.exit('You need set the GITHUB_REPOSITORY')

    url_owner_issues = f'https://api.github.com/repos/{repository}/issues'
    issues = get_issues(URL_REPO_ISSUES)
    issues_owner = get_issues(url_owner_issues)
    issues_owner_title = [issue.get('title') for issue in issues_owner]

    dir_issues = Path('build/issues')

    if not dir_issues.is_dir():
        dir_issues.mkdir()

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
            if create_issue(issue, url_owner_issues, token):
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
    _token = args.token
    _repository = args.repo
    main(_token, _repository)
