## TL;DR
Some methods to include to make sure Jupyter Notebook run smoothly

### Article Link
https://towardsdatascience.com/7-setups-you-should-include-at-the-beginning-of-a-data-science-project-8232ab10a1ec

## Useful Code Snippets
```python
# Ensure package version
import tensorflow as tf
assert tf.__version__ >= "2.0"
# Ouput multiple results in one cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


