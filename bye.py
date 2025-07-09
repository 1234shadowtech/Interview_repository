```python
def calculate_area(shape, *args):  # Function to calculate the area of different shapes
    if shape == "circle":
        if len(args) != 1:  # Validate the number of arguments for a circle
            raise ValueError("Circle requires exactly 1 argument: radius")
        radius = args[0]  # Assumes the first argument is the radius
        return 3.14159 * radius * radius  # Area of a circle = πr² (Consider using math.pi for accuracy)
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
        return None  # Returns None for unsupported shapes (Consider raising NotImplementedError)

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
        else:  # Handle unsupported data types
            raise TypeError(f"Unsupported data type: {type(item)}")  # Consider handling unsupported types more gracefully
    return result  # Return the processed list

def validate_user(username, password):  # Function to validate a username and password
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

def format_output(data, format_type):  # Function to format data into different formats
    import json  # Import the JSON module (Move to top of file for better organization)
    import csv  # Import the CSV module (Move to top of file for better organization)
    import io  # Import the IO module for in-memory file handling (Move to top of file for better organization)
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
        return str(data)  # Convert the data to a string for unsupported formats

def main():  # Main function to demonstrate the functionality
    print(calculate_area("circle", 5))  # Calculate and print the area of a circle
    print(calculate_area("rectangle", 4, 7))  # Calculate and print the area of a rectangle
    print(process_data([1, 2, 3, "hello"]))  # Process and print a list of data
    print(validate_user("admin", "Password123!"))  # Validate and print the result for a username and password
    print(format_output([["a", "b"], ["c", "d"]], "csv"))  # Format and print data as CSV

if __name__ == "__main__":  # Entry point of the script
    main()  # Call the main function
```