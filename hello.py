```python
def analyze_text(text):
    stats = {}
    stats['length'] = len(text)  # Calculate the total number of characters in the text
    stats['words'] = len(text.split())  # Count the number of words by splitting the text on whitespace
    stats['uppercase'] = sum(1 for c in text if c.isupper())  # Count the number of uppercase letters
    stats['lowercase'] = sum(1 for c in text if c.islower())  # Count the number of lowercase letters
    stats['digits'] = sum(1 for c in text if c.isdigit())  # Count the number of numeric digits
    return stats

def filter_products(products, min_price=0, max_price=1000, category=None):
    filtered = []  # Initialize an empty list to store filtered products
    for p in products:  # Iterate through each product in the list
        if p['price'] >= min_price and p['price'] <= max_price:  # Check if the product's price is within the range
            if category is None or p['category'] == category:  # Check if the category matches or is not specified
                filtered.append(p)  # Add the product to the filtered list
    return filtered

def generate_report(data, output_file=None):
    report = []  # Initialize an empty list to store the report lines
    report.append(f"Report generated on: {datetime.now()}")  # Add the current timestamp to the report
    report.append(f"Total items: {len(data)}")  # Add the total number of items in the data
    
    if isinstance(data[0], dict):  # Check if the first item in the data is a dictionary
        keys = data[0].keys()  # Extract the keys (column names) from the dictionary
        report.append("\nColumns: " + ", ".join(keys))  # Add the column names to the report
    
    if output_file:  # Check if an output file is specified
        with open(output_file, 'w') as f:  # Open the file in write mode
            f.write("\n".join(report))  # Write the report lines to the file
    return "\n".join(report)  # Return the report as a single string

def calculate_stats(numbers):
    if not numbers:  # Check if the list of numbers is empty
        return None  # Return None if there are no numbers
    
    stats = {}  # Initialize an empty dictionary to store statistics
    stats['mean'] = sum(numbers) / len(numbers)  # Calculate the mean (average) of the numbers
    stats['min'] = min(numbers)  # Find the minimum value in the list
    stats['max'] = max(numbers)  # Find the maximum value in the list
    stats['range'] = stats['max'] - stats['min']  # Calculate the range (difference between max and min)
    
    sorted_nums = sorted(numbers)  # Sort the numbers in ascending order
    mid = len(sorted_nums) // 2  # Find the middle index of the sorted list
    stats['median'] = (sorted_nums[mid] + sorted_nums[~mid]) / 2  # Calculate the median (middle value)
    
    return stats

def process_user_input(input_str):
    try:
        if input_str.lower() == 'exit':  # Check if the input is the 'exit' command
            return False  # Return False to indicate the program should exit
        elif input_str.startswith('calc '):  # Check if the input starts with 'calc '
            expr = input_str[5:]  # Extract the mathematical expression after 'calc '
            return eval(expr)  # Evaluate the expression and return the result
        elif input_str.startswith('repeat '):  # Check if the input starts with 'repeat '
            text, times = input_str[7:].split(maxsplit=1)  # Extract the text and repetition count
            return text * int(times)  # Repeat the text the specified number of times
        else:
            return input_str.upper()  # Convert the input to uppercase if no other conditions are met
    except:  # Handle any exceptions that occur during processing
        return "Invalid input"  # Return an error message for invalid input

if __name__ == "__main__":
    from datetime import datetime  # Import the datetime module for timestamp generation
    
    sample_text = "Hello World! 123"  # Example text for analysis
    print(analyze_text(sample_text))  # Analyze the sample text and print the statistics
    
    products = [
        {'name': 'A', 'price': 100, 'category': 'X'},  # Example product with name, price, and category
        {'name': 'B', 'price': 200, 'category': 'Y'},  # Another example product
    ]
    print(filter_products(products, 150, 250))  # Filter products within a price range and print the result
    
    print(generate_report(products))  # Generate a report for the products and print it
    
    numbers = [1, 2, 3, 4, 5]  # Example list of numbers for statistical analysis
    print(calculate_stats(numbers))  # Calculate statistics for the numbers and print the result
    
    print(process_user_input("calc 5+3"))  # Process a calculation input and print the result
    print(process_user_input("repeat abc 3"))  # Process a repeat input and print the result
```