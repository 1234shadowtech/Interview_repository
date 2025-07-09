```python
import math  # Import math module for mathematical constants and functions
import json  # Import JSON module for JSON formatting
import csv  # Import CSV module for CSV formatting
import io  # Import IO module for in-memory file handling

def calculate_area(shape: str, *args) -> float:  # Function to calculate the area of different shapes
    """
    Calculate the area of a given shape.
    :param shape: The type of shape ('circle', 'rectangle', 'triangle').
    :param args: Dimensions of the shape.
    :return: Area of the shape.
    """
    if shape == "circle":
        if len(args) != 1:  # Validate the number of arguments for a circle
            raise ValueError("Circle requires exactly 1 argument: radius")
        radius = args[0]  # Assumes the first argument is the radius
        return math.pi * radius * radius  # Use math.pi for better accuracy
    elif shape == "rectangle":
        if len(args) != 2:  # Validate the number of arguments for a rectangle
            raise ValueError("Rectangle requires exactly 2 arguments: length and width")
        length, width = args  # Assumes two arguments: length and width
        return length * width  # Area of a rectangle = length × width
    elif shape == "triangle":
        if len(args) != 2:  # Validate the number of arguments for a triangle
            raise ValueError("Triangle requires exactly 2 arguments: base and height")
        base, height = args  # Assumes two arguments: base and height
        return 0.5 * base * height  # Area of a triangle = 0.5 × base × height
    else:
        raise NotImplementedError(f"Shape '{shape}' is not supported")  # Explicit error for unsupported shapes

def process_data(data: list) -> list:  # Function to process a list of data
    """
    Process a list of data by transforming integers and strings.
    :param data: List of data items (int, str).
    :return: Processed list.
    """
    result = []  # Initialize an empty list to store results
    for item in data:  # Iterate over each item in the input data
        if isinstance(item, int):  # Check if the item is an integer
            if item % 2 == 0:  # Check if the integer is even
                result.append(item * 2)  # Double the even integer
            else:
                result.append(item * 3)  # Triple the odd integer
        elif isinstance(item, str):  # Check if the item is a string
            result.append(item.upper())  # Convert the string to uppercase
        else:  # Handle unsupported data types
            # Log or skip unsupported types instead of raising an error
            print(f"Warning: Unsupported data type {type(item)}. Skipping...")
    return result  # Return the processed list

def validate_user(username: str, password: str) -> bool:  # Function to validate a username and password
    """
    Validate a username and password based on length and complexity requirements.
    :param username: The username to validate.
    :param password: The password to validate.
    :return: True if valid, False otherwise.
    """
    if len(username) < 4:  # Check if the username is too short
        return False
    if len(password) < 8:  # Check if the password is too short
        return False
    # Combine all checks into a single loop for better performance
    has_digit = has_upper = has_special = False
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif not char.isalnum():  # Check for special characters
            has_special = True
        # Break early if all conditions are met
        if has_digit and has_upper and has_special:
            break
    if not (has_digit and has_upper and has_special):  # Ensure all conditions are met
        return False
    return True  # Return True if all conditions are met

def format_output(data: list, format_type: str) -> str:  # Function to format data into different formats
    """
    Format data into JSON or CSV format.
    :param data: The data to format.
    :param format_type: The format type ('json', 'csv').
    :return: Formatted data as a string.
    """
    if format_type == "json":
        return json.dumps(data)  # Convert the data to a JSON string
    elif format_type == "csv":
        if not all(isinstance(row, (list, tuple)) for row in data):  # Validate data structure for CSV
            raise ValueError("Data must be a list of lists or tuples for CSV format")
        output = io.StringIO()  # Create an in-memory file object
        writer = csv.writer(output)  # Create a CSV writer object
        for row in data:  # Iterate over each row in the data
            writer.writerow(row)  # Write the row to the CSV
        return output.getvalue()  # Return the CSV content as a string
    else:
        raise ValueError(f"Unsupported format type: {format_type}")  # Explicit error for unsupported formats

def main():  # Main function to demonstrate the functionality
    """
    Demonstrate the functionality of the script.
    """
    print(calculate_area("circle", 5))  # Calculate and print the area of a circle
    print(calculate_area("rectangle", 4, 7))  # Calculate and print the area of a rectangle
    print(process_data([1, 2, 3, "hello"]))  # Process and print a list of data
    print(validate_user("admin", "Password123!"))  # Validate and print the result for a username and password
    print(format_output([["a", "b"], ["c", "d"]], "csv"))  # Format and print data as CSV

if __name__ == "__main__":  # Entry point of the script
    main()  # Call the main function
```