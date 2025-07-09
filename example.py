```python
def calculate_area(radius):
    # Function to calculate the area of a circle given its radius
    pi = 3.14159  # Define the value of pi
    return pi * radius ** 2  # Return the area using the formula: pi * radius^2

def print_area(radius):
    # Function to print the area of a circle
    area = calculate_area(radius)  # Call calculate_area to get the circle's area
    print(f"The area of the circle with radius {radius} is {area}")  # Print the result

# Main execution starts here
radius = 5  # Define the radius of the circle
print_area(radius)  # Call print_area to display the area of the circle
```