## TL;DR
<<<<<<< HEAD
The basis to build a customized model in Scikit-learn, it is like writing a Python class

### Article Link
https://towardsdatascience.com/building-a-custom-model-in-scikit-learn-b0da965a1299

### Author
Tim Book
=======
Tools to visualize your data and plot in Jupyter Notebook interactively

### Article Link
https://towardsdatascience.com/jupyter-superpower-interactive-visualization-combo-with-python-ffc0adb37b7b

### Author
>>>>>>> 3a848a5b5940b78e03566184dfe0828f86b77e02

## Key Takeaways
* You can create you customized model, the methods that every Scikit-learn model has are:
  * .fit()
  * .predict()
  * .score()
  * .set_params()
  * .get_params()

* You can add all other methods you can imagine.

## Useful Code Snippets
```python
<<<<<<< HEAD
from self.preprocessing import OneHotEncoder
class KMeansTransformer(TransformerMixin):
    def __init__(self, *args, **args):
        self.model = KMeans(*args, **args)
    def fit(self, X):
        self.X = X
        self.model.fit(X)
    def transform(self, X):
        # Need to reshape into a column vector in order to use
        # the onehot encoder.
        cl = self.model.predict(X).reshape(-1, 1)
        
        self.oh = OneHotEncoder(
            categories="auto", 
            sparse=False,
            drop="first"
        )
        cl_matrix = self.oh.fit_transform(cl)      
 
        return np.hstack([self.X, cl_matrix])
    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)
=======
import qgrid
gqrid_widget = qgrid.show_grid(cars)
>>>>>>> 3a848a5b5940b78e03566184dfe0828f86b77e02

```

## Useful Tools
<<<<<<< HEAD
* 
* 
=======
*  `qgrid` let you have an Excel-like table inside Jupyter Notebook/Lab
>>>>>>> 3a848a5b5940b78e03566184dfe0828f86b77e02

## Comments/ Questions
