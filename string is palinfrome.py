def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

word = "madam"

print(is_palindrome(word))
# Output: True