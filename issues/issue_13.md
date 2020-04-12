## TL;DR
<<<<<<< HEAD
This article looks at how to tokenize and prepare text data with TensorFlow and Keras preprocessing tools 

### Article Link
https://www.kdnuggets.com/2020/03/tensorflow-keras-tokenization-text-data-prep.html

### Author
Matthew Mayo

## Key Takeaways

## Useful Code Snippets
```python
# Tokenize our training data
tokenizer = Tokenizer(num_words=num_words, oov_token=oov_token)
tokenizer.fit_on_texts(train_data)

# Get our training data word index
word_index = tokenizer.word_index

# Encode training data sentences into sequences
train_sequences = tokenizer.texts_to_sequences(train_data)

# Get max training sequence length
maxlen = max([len(x) for x in train_sequences])

# Pad the training sequences
train_padded = pad_sequences(train_sequences, padding=pad_type, truncating=trunc_type, maxlen=maxlen)
```

## Useful Tools
* Keras
* TensorFlow
=======
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
>>>>>>> 3a848a5b5940b78e03566184dfe0828f86b77e02

## Comments/ Questions
