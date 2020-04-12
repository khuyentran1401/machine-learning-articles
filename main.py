#!/usr/bin/env python
# coding: utf-8

from pathlib import Path
import requests
# Machine Learning Articles
URL_REPO_ISSUES = 'https://api.github.com/repos/khuyentran1401/machine-learning-articles/issues'
# TODO: Issues per_pages
issues = requests.get(URL_REPO_ISSUES).json()

WORKFLOW_TEMPLATE = """
name: Create Issues

on: 
  release:
    types: [created]

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v1
    - name: Fetch Issues from repository
      shell: bash
      run: |
        pip install -r requirements.txt
        python main.py
        git config --global user.name 'oleksis'
        git config --global user.email 'oleksis.fraga@gmail.com'
        git add .
        git commit --allow-empty -am "Update workflow"
        git push origin HEAD:master
"""

dir_issues = Path('issues')
issues_files = []
if not dir_issues.is_dir():
    dir_issues.mkdir()
else:
    issues_files= [int(file.stem.split('_')[1])
                   for file in Path().glob(f'{dir_issues}/issue_*.md')]

file_name = 'ciff.yml'

with open(file_name, 'w') as file_yml:
    file_yml.write(WORKFLOW_TEMPLATE)

file_yml = open(file_name, 'a+')
for issue in issues:
    number = issue.get('number')
    if not number in issues_files:
        title = issue.get('title')
        file_name = f'issue_{number}'
        user = issue.get('user').get('login')
        labels = ", ".join(lab.get('name') for lab in issue.get('labels'))
        body = issue.get('body')

        with open(f'{dir_issues}/{file_name}.md', 'w') as file_md:
            file_md.write(body)

        JOB_TEMPLATE = f"""
    - name: Create Issue From File
      uses: peter-evans/create-issue-from-file@v2
      with:
        title: "{title}"
        content-filepath: "./{dir_issues}/{file_name}.md"
        labels: {labels}
        project: Machine Learning Articles
        project-column: To do
"""
        file_yml.write(JOB_TEMPLATE)
    
file_yml.close()
