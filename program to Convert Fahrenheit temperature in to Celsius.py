# Program to convert Fahrenheit temperature to Celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

# Example usage
fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Fahrenheit is equal to {celsius_temp:.2f} Celsius")