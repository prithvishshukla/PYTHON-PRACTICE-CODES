def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example usage
x = input("Enter the first number (x): ")
y = input("Enter the second number (y): ")

# Swapping using a temporary variable
x, y = swap_with_temp(x, y)
print(f"swapped value (x:y) : ({x}:{y})")

