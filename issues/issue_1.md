<<<<<<< HEAD
## TL;DR
Overview about types of classification tasks and which algorithms to use with each task

### Article Link
https://machinelearningmastery.com/types-of-classification-in-machine-learning/

### Author
Jason Brownlee

## Key Takeaways
4 main type of classification tasks
* Binary Classification: 0 or 1
* Multi-Class Classification: model predicts the probability of an example belonging to each class label.
* Multi-Label Classification: classification tasks that have two or more class labels, where one or more class labels may be predicted for each example.
* Imbalanced Classification: classification tasks where the number of examples in each class is unequally distributed.

## Useful Code Snippets


## Useful Tools

## Comments/ Questions
=======
## TL;DR
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

## Comments/ Questions
>>>>>>> 3a848a5b5940b78e03566184dfe0828f86b77e02
