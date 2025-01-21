import math

def calculate_shape_properties(shape, *args):
    if shape == "circle":
        radius = args[0]
        return {"Area": math.pi * radius ** 2, "Perimeter": 2 * math.pi * radius}
    elif shape == "rectangle":
        length, width = args
        return {"Area": length * width, "Perimeter": 2 * (length + width)}
    elif shape == "square":
        side = args[0]
        return {"Area": side ** 2, "Perimeter": 4 * side}
    elif shape == "triangle":
        base, height, a, b, c = args
        return {"Area": 0.5 * base * height, "Perimeter": a + b + c}
    else:
        return "Sorry, I don't recognize that shape."

shape = input("Enter the shape (circle, rectangle, square, triangle): ").lower()

if shape in ["circle", "square"]:
    dimension = float(input(f"Enter the {shape} dimension: "))
    properties = calculate_shape_properties(shape, dimension)
elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    properties = calculate_shape_properties(shape, length, width)
elif shape == "triangle":
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    a = float(input("Enter the first side of the triangle: "))
    b = float(input("Enter the second side of the triangle: "))
    c = float(input("Enter the third side of the triangle: "))
    properties = calculate_shape_properties(shape, base, height, a, b, c)
else:
    properties = "Sorry, I don't recognize that shape."

if isinstance(properties, dict):
    for key, value in properties.items():
        print(f"{shape.capitalize()}: {key} = {value}")
else:
    print(properties)