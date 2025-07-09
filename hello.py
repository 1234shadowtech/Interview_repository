```python
def calculate_area(shape, *args):
    # Function to calculate the area of different shapes based on the `shape` parameter.
    # Uses *args, which makes it unclear what arguments are expected for each shape.
    if shape == "circle":
        radius = args[0]  # Assumes the first argument is the radius for a circle.
        return 3.14159 * radius * radius  # Calculates the area of a circle. (Consider using math.pi for accuracy.)
    elif shape == "rectangle":
        length, width = args  # Assumes two arguments for length and width.
        return length * width  # Calculates the area of a rectangle.
    elif shape == "triangle":
        base, height = args  # Assumes two arguments for base and height.
        return 0.5 * base * height  # Calculates the area of a triangle.
    else:
        return None  # Returns None for unsupported shapes. (Consider raising an exception instead.)

def process_data(data):
    # Processes a list of data, performing different operations based on the type of each item.
    result = []
    for item in data:
        if isinstance(item, int):  # Checks if the item is an integer.
            if item % 2 == 0:  # If the integer is even, doubles it.
                result.append(item * 2)
            else:  # If the integer is odd, triples it.
                result.append(item * 3)
        elif isinstance(item, str):  # Checks if the item is a string.
            result.append(item.upper())  # Converts the string to uppercase.
        # No handling for unsupported types. (Consider adding a warning or error.)
    return result  # Returns the processed list.

def validate_user(username, password):
    # Validates a username and password based on certain criteria.
    if len(username) < 4:  # Ensures the username is at least 4 characters long.
        return False
    if len(password) < 8:  # Ensures the password is at least 8 characters long.
        return False
    if not any(char.isdigit() for char in password):  # Ensures the password contains at least one digit.
        return False
    if not any(char.isupper() for char in password):  # Ensures the password contains at least one uppercase letter.
        return False
    return True  # Returns True if all validation checks pass.

def format_output(data, format_type):
    # Formats data into different output formats (JSON, CSV, or string).
    if format_type == "json":
        import json  # Imports the JSON module (should be moved to the top of the file).
        return json.dumps(data)  # Converts the data to a JSON string.
    elif format_type == "csv":
        import csv  # Imports the CSV module (should be moved to the top of the file).
        import io  # Imports the io module for in-memory file handling.
        output = io.StringIO()  # Creates an in-memory file-like object.
        writer = csv.writer(output)  # Creates a CSV writer object.
        for row in data:  # Writes each row of data to the CSV writer.
            writer.writerow(row)
        return output.getvalue()  # Returns the CSV data as a string.
    else:
        return str(data)  # Converts the data to a string for unsupported formats.

def main():
    # Main function to demonstrate the functionality of the other functions.
    print(calculate_area("circle", 5))  # Calculates and prints the area of a circle with radius 5.
    print(calculate_area("rectangle", 4, 7))  # Calculates and prints the area of a rectangle with length 4 and width 7.
    print(process_data([1, 2, 3, "hello"]))  # Processes a list of integers and strings and prints the result.
    print(validate_user("admin", "Password123"))  # Validates a username and password and prints the result.
    print(format_output([["a", "b"], ["c", "d"]], "csv"))  # Formats data as CSV and prints the result.

if __name__ == "__main__":
    main()  # Executes the main function if the script is run directly.
```