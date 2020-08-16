## TL;DR
Why and how to use pipenv
### Article Link
https://realpython.com/pipenv-guide/
## Key Takeaways
*  Pipenv is a combo of virtualenv and pip
* The sub-dependencies are not shown in Pipfile, which makes is more simplified than requirements.txt
* You don't need to specify the environment for every package to make sure the code or installation does not break in the future
* Pyfile.lock locks the exact requirements for a package. It also handles the subdependencies

## Code snippets
* `pipenv shell`: create and activate virtualenv
*  `pipenv install <package>`
* `pipenv install <package> --dev`: install package for development
*  `pipenv lock`: similar to `pip freeze >> requirements.txt`
*  `pipenv check`
*  `pipenv --venv`: find the directory of virtual env

## Useful Tools
*  pipenv