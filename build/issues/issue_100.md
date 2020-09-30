## TL;DR
How to migrate from jupyter notebooks to scripts for reproducibility
### Article Link
https://towardsdatascience.com/from-jupyter-notebook-to-sc-582978d3c0c
### Author
https://towardsdatascience.com/from-jupyter-notebook-to-sc-582978d3c0c
## Key Takeaways
*  Configure parameters with config
*  Collect the outputs in a file with logging. Alternative: MLFlow or Wandb
*  Make sure the code does not break with pytest
* Continuous integration: run unit tests automatically. -> Github Action
* Make sure the model works in any computer: Docker

