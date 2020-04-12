## TL;DR
<<<<<<< HEAD
Use DVC for versioning large data files

### Article Link
https://blog.usejournal.com/version-control-for-data-science-tracking-your-machine-learning-models-and-datasets-aaa61f20bb45

### Author
Vipul J

## Key Takeaways
*  Make it easy to track the artifacts, which is important for reproducibility
=======
An efficient workflow for data science

### Article Link
https://towardsdatascience.com/good-coding-practices-for-data-science-e9237783784c

### Author

## Key Takeaways
### Code organization
* **Specification Files**: Files to specify various parameters for the code (YAML or JSON). Benefit: use the code in different ways with no code changes
* **Utilities**: Save the files that are reproducible and generic for future projects. 
*  **Core Functionality**: Separate the pipeline of your project into different files (data extraction, data exploration, data engineering, modeling). Benefit: Easy to change and manipulate the file without running the entire code. Organize your projects for easy reviewing
* **Main Executable**: `main.py` for execute the entire code. Should be short for someone else to understand how pieces of files are integrated together
>>>>>>> 3a848a5b5940b78e03566184dfe0828f86b77e02

### Documentation
Maintain a **Readme page** for keeping track of the code changes. Useful for others to look at your code and understand how to use it.  

### Commenting
Comment on the top of every file for you to organize and for reader to understand the function of the files

### Version Control
Benefits: collaborations, can switch back to the older version. Useful for experimenting, editing, and comparing different versions

<<<<<<< HEAD
## Useful Tools
*  DVC

## Comments/ Questions
* Are you using DVC? If yes, how do you integrate it into your data science practice?
=======
### Automated testing
Use unittest to validate the functionality of different parts of the code

## Useful Code Snippets

## Useful Tools

## Comments/ Questions
* Knowing these helpful techniques, we should gradually adopt these practices for efficient project management
* Things that we could add into this workflow:

1. Mectrics and logging to keep track of metrics and data with [MlFlow](https://mlflow.org/)
1. A tool to easily create a comprehensible config with [Hydra.cc](https://hydra.cc/)
1. If the workflow of one project seems to be efficient to us, we can create a template with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
>>>>>>> 3a848a5b5940b78e03566184dfe0828f86b77e02
