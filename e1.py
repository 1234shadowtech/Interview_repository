```python
def calculate_area(shape, dimensions):
    # Check the shape type to determine the formula for area calculation
    if shape == "circle":
        # Ensure dimensions is a single value (radius) for a circle
        radius = dimensions[0]
        # Calculate area of the circle using πr^2
        return 3.14159 * (radius ** 2)
    elif shape == "rectangle":
        # Ensure dimensions contains two values (length and width) for a rectangle
        length, width = dimensions
        # Calculate area of the rectangle using length * width
        return length * width
    elif shape == "triangle":
        # Ensure dimensions contains two values (base and height) for a triangle
        base, height = dimensions
        # Calculate area of the triangle using 0.5 * base * height
        return 0.5 * base * height
    else:
        # Handle unsupported shape types
        raise ValueError("Unsupported shape type")
        # Raise an exception to notify the caller about invalid input
```