from nltk.tokenize import word_tokenize

def combine_words(text, x):
    split_words = word_tokenize(text)
    combined_words = []

    # Iterate over the split words in steps of x
    for i in range(0, len(split_words), x):
        # Combine x words into a single string
        combined_word = ' '.join(split_words[i:i+x])
        combined_words.append(combined_word)

    return combined_words

def combine_words_from_split_words(split_words, x):
    combined_words = []

    # Iterate over the split words in steps of x
    for i in range(0, len(split_words), x):
        # Combine x words into a single string
        combined_word = ' '.join(split_words[i:i+x])
        combined_words.append(combined_word)

    return combined_words

if __name__ == "__main__":
    text = "This is a sample text to demonstrate the combination of words."
    x = 3  # Number of words to combine
    combined_words = combine_words(text, x)
    combined_words_from_split_words = combine_words_from_split_words(text, x)
    print("Combined words:")
    print(combined_words)
    print("Combined words from split words:")
    print(combined_words_from_split_words)