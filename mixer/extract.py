import random
from save_to_file import saveToFile
from words import combine_words_from_split_words
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
# Download the Punkt tokenizer data (only needed once)
nltk.download('punkt')
def extract_sentences(dataset,sample_size,dataset_name,column_name):
  # Initialize an empty list to store the sentences
  sentences = []
  # Initialize an empty list to store the words
  words = []

  # Iterate over the dataset and split the text into sentences
  for example in dataset.shuffle():
      text = example[column_name]
      # SENTENCE
      # Split the text into sentences
      split_sentences = sent_tokenize(text)
      # Extend the list with the split sentences
      sentences.extend(split_sentences)

      # WORD
      # Split the text into words
      split_words = word_tokenize(text)
      combined_words = combine_words_from_split_words(split_words, 5)
      # Extend the list with the split words
      words.extend(combined_words)

  #Filter words
  words=[word for word in words if any(c.isalnum() for c in word)]

  # Shuffle the sentences and words list
  random.shuffle(sentences)
  random.shuffle(words)
  mix=sentences+words
  random.shuffle(mix)
  # Truncate the sentences list to the first 50 sentences
  sentences = sentences[:sample_size]
  words = words[:sample_size]
  mix = mix[:sample_size]

  # Optionally, save the JSON array to a file
#   saveToFile("sentence",dataset_name,sentences)
#   saveToFile("word",dataset_name,words)
#   saveToFile("mix",dataset_name,mix)
  return sentences, words, mix