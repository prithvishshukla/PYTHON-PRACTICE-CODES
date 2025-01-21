def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

# Example usage
input_string = "Hello, World!"
length = string_length(input_string)
print(f"The length of the string is: {length}")