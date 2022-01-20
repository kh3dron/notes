# Transformers from Scratch
# https://e2eml.school/transformers.html#one_hot

- One Hot Encoding
  - store entire vocabulary as an array, each word becomoes a vector of all 0's but the word's position as a 1
  - You could dot product a word with a vector to show how well that word is represented in the sentence
- Matrix as lookup table
  - Row is a word, Columns are probabilities of that word coming next
  - 