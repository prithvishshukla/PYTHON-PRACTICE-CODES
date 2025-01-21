def count_words(input_string):
    words = input_string.split()
    return len(words)

# Example usage
input_string = "Write a program to count number of words in a multi word string"
word_count = count_words(input_string)
print(f"The number of words in the string is: {word_count}")