```python
def calculate_area(shape, *args):  # Function to calculate the area of different shapes
    if shape == "circle":
        radius = args[0]  # Assumes the first argument is the radius
        return 3.14159 * radius * radius  # Area of a circle = πr²
    elif shape == "rectangle":
        length, width = args  # Assumes two arguments: length and width
        return length * width  # Area of a rectangle = length × width
    elif shape == "triangle":
        base, height = args  # Assumes two arguments: base and height
        return 0.5 * base * height  # Area of a triangle = 0.5 × base × height
    else:
        return None  # Returns None for unsupported shapes

def process_data(data):  # Function to process a list of data
    result = []  # Initialize an empty list to store results
    for item in data:  # Iterate over each item in the input data
        if isinstance(item, int):  # Check if the item is an integer
            if item % 2 == 0:  # Check if the integer is even
                result.append(item * 2)  # Double the even integer
            else:
                result.append(item * 3)  # Triple the odd integer
        elif isinstance(item, str):  # Check if the item is a string
            result.append(item.upper())  # Convert the string to uppercase
    return result  # Return the processed list

def validate_user(username, password):  # Function to validate a username and password
    if len(username) < 4:  # Check if the username is too short
        return False
    if len(password) < 8:  # Check if the password is too short
        return False
    if not any(char.isdigit() for char in password):  # Check if the password contains a digit
        return False
    if not any(char.isupper() for char in password):  # Check if the password contains an uppercase letter
        return False
    return True  # Return True if all conditions are met

def format_output(data, format_type):  # Function to format data into different formats
    if format_type == "json":
        import json  # Import the JSON module
        return json.dumps(data)  # Convert the data to a JSON string
    elif format_type == "csv":
        import csv  # Import the CSV module
        import io  # Import the IO module for in-memory file handling
        output = io.StringIO()  # Create an in-memory file object
        writer = csv.writer(output)  # Create a CSV writer object
        for row in data:  # Iterate over each row in the data
            writer.writerow(row)  # Write the row to the CSV
        return output.getvalue()  # Return the CSV content as a string
    else:
        return str(data)  # Convert the data to a string for unsupported formats

def main():  # Main function to demonstrate the functionality
    print(calculate_area("circle", 5))  # Calculate and print the area of a circle
    print(calculate_area("rectangle", 4, 7))  # Calculate and print the area of a rectangle
    print(process_data([1, 2, 3, "hello"]))  # Process and print a list of data
    print(validate_user("admin", "Password123"))  # Validate and print the result for a username and password
    print(format_output([["a", "b"], ["c", "d"]], "csv"))  # Format and print data as CSV

if __name__ == "__main__":  # Entry point of the script
    main()  # Call the main function
```