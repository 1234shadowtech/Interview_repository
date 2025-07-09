```python
# Function to calculate the area of different shapes
def calculate_area(shape, *args):
    # Check the shape type and calculate the area accordingly
    if shape == "circle":
        radius = args[0]  # Assumes the first argument is the radius
        return 3.14159 * radius * radius  # Suggest using math.pi for better precision
    elif shape == "rectangle":
        length, width = args  # Assumes two arguments: length and width
        return length * width
    elif shape == "triangle":
        base, height = args  # Assumes two arguments: base and height
        return 0.5 * base * height
    else:
        return None  # Returns None for unsupported shapes (could raise an exception instead)

# Function to process a list of data
def process_data(data):
    result = []  # Initialize an empty list to store processed results
    for item in data:
        if isinstance(item, int):  # Check if the item is an integer
            if item % 2 == 0:  # If the integer is even
                result.append(item * 2)  # Multiply by 2
            else:  # If the integer is odd
                result.append(item * 3)  # Multiply by 3
        elif isinstance(item, str):  # Check if the item is a string
            result.append(item.upper())  # Convert the string to uppercase
        # No handling for unsupported types (e.g., floats, lists, etc.)
    return result

# Function to validate a username and password
def validate_user(username, password):
    # Check if the username is at least 4 characters long
    if len(username) < 4:
        return False
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    return True  # Return True if all conditions are met

# Function to format data into different output types
def format_output(data, format_type):
    if format_type == "json":
        import json  # Importing json module (should be moved to the top of the file)
        return json.dumps(data)  # Convert data to JSON format
    elif format_type == "csv":
        import csv  # Importing csv module (should be moved to the top of the file)
        import io  # Importing io module (should be moved to the top of the file)
        output = io.StringIO()  # Create an in-memory string buffer
        writer = csv.writer(output)  # Initialize a CSV writer
        for row in data:  # Iterate over rows in the data
            writer.writerow(row)  # Write each row to the CSV
        return output.getvalue()  # Return the CSV content as a string
    else:
        return str(data)  # Convert data to a string for unsupported formats

# Main function to test the above functions
def main():
    # Test calculate_area function with different shapes
    print(calculate_area("circle", 5))  # Circle with radius 5
    print(calculate_area("rectangle", 4, 7))  # Rectangle with length 4 and width 7
    # Test process_data function with a mixed list
    print(process_data([1, 2, 3, "hello"]))  # List containing integers and a string
    # Test validate_user function with a sample username and password
    print(validate_user("admin", "Password123"))  # Valid username and password
    # Test format_output function with CSV format
    print(format_output([["a", "b"], ["c", "d"]], "csv"))  # List of lists formatted as CSV

# Entry point of the script
if __name__ == "__main__":
    main()
```