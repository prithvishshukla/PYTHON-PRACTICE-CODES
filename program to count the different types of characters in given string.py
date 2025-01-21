def count_characters(s):
    counts = {
        'uppercase': 0,
        'lowercase': 0,
        'digits': 0,
        'special': 0
    }
    
    for char in s:
        if char.isupper():
            counts['uppercase'] += 1
        elif char.islower():
            counts['lowercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        else:
            counts['special'] += 1
    
    return counts

# Example usage
input_string = "Hello World! 123"
result = count_characters(input_string)
print(result)