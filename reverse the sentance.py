def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

text = "Python is fun"
print(reverse_words(text))