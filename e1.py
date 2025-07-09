```python
def calculate_area(shape, *args):
    # Check the shape type and calculate the area accordingly
    if shape == "circle":
        radius = args[0]  # Extract the radius from the arguments
        return 3.14159 * radius * radius  # Calculate the area of the circle
    elif shape == "rectangle":
        length, width = args  # Extract length and width from the arguments
        return length * width  # Calculate the area of the rectangle
    elif shape == "triangle":
        base, height = args  # Extract base and height from the arguments
        return 0.5 * base * height  # Calculate the area of the triangle
    else:
        return None  # Return None for unsupported shapes

def process_data(data):
    # Initialize an empty list to store the processed results
    result = []
    for item in data:
        # Check if the item is an integer
        if isinstance(item, int):
            if item % 2 == 0:  # Check if the integer is even
                result.append(item * 2)  # Double the even integer
            else:
                result.append(item * 3)  # Triple the odd integer
        # Check if the item is a string
        elif isinstance(item, str):
            result.append(item.upper())  # Convert the string to uppercase
    return result  # Return the processed data

def validate_user(username, password):
    # Validate the username length
    if len(username) < 4:
        return False
    # Validate the password length
    if len(password) < 8:
        return False
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    return True  # Return True if all validations pass

def format_output(data, format_type):
    # Check if the format type is JSON
    if format_type == "json":
        import json  # Import the JSON module
        return json.dumps(data)  # Convert the data to a JSON string
    # Check if the format type is CSV
    elif format_type == "csv":
        import csv  # Import the CSV module
        import io  # Import the IO module for in-memory file handling
        output = io.StringIO()  # Create an in-memory text stream
        writer = csv.writer(output)  # Create a CSV writer object
        for row in data:
            writer.writerow(row)  # Write each row to the CSV
        return output.getvalue()  # Return the CSV content as a string
    else:
        return str(data)  # Convert the data to a string for unsupported formats

def main():
    # Test the calculate_area function with different shapes
    print(calculate_area("circle", 5))  # Circle with radius 5
    print(calculate_area("rectangle", 4, 7))  # Rectangle with length 4 and width 7
    # Test the process_data function with a mixed list
    print(process_data([1, 2, 3, "hello"]))
    # Test the validate_user function with a sample username and password
    print(validate_user("admin", "Password123"))
    # Test the format_output function with CSV format
    print(format_output([["a", "b"], ["c", "d"]], "csv"))

# Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
```