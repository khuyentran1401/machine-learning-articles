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
