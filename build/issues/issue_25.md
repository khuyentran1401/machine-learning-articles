## TL;DR
What is OOP and why it is important?

### Article Link
https://towardsdatascience.com/object-oriented-programming-for-data-scientists-build-your-ml-estimator-7da416751f64

### Author
Tirthajyoti Sarkar

## Key Takeaways
### What is OOP?
Create classes for abstract data 
### Why should we care about OOP?
*  Group similar abstract data together so that the code is organized 
*  If we want to perform some methods on a specific data, we call the class and its method

```python
import matplotlib.pyplot as pt
```
`.pyplot` is the method of the class `matplotlib`

Think about it. How do you use `linear_model` from `sklearn`. You would call
```python 
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit()
```
`LinearRegression` is a class of linear regression model. Since the `.fit()` of `lm` is different from the `.fit()` of other models, this is where OOP is really useful

## Useful Tools
## Comments/ Questions

