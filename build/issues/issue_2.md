## TL;DR
The basis to build a customized model in Scikit-learn, it is like writing a Python class

### Article Link
https://towardsdatascience.com/building-a-custom-model-in-scikit-learn-b0da965a1299

### Author
Tim Book

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

```

## Useful Tools
* 
* 

## Comments/ Questions
