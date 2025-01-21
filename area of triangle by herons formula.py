import math
# Taking input for the three sides of the triangle
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
# Calculating the perimeter
perimeter = a + b + c
print("Perimeter of the triangle:", perimeter)
# Using Heron's formula to calculate the area
# Semi-perimeter (s)
s = perimeter / 2
# Area calculation
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of the triangle:", area)