def remove_consonants(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in input_string if char in vowels or not char.isalpha()])
    return result

# Get input from the user
input_string = input("Enter a string: ")
output_string = remove_consonants(input_string)
print("String after removing consonants:", output_string)