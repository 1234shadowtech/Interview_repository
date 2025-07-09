```python
# Function to analyze text and return statistics
def analyze_text(text):
    stats = {}
    stats['length'] = len(text)  # Total length of the text
    stats['words'] = len(text.split())  # Number of words in the text
    stats['uppercase'] = sum(1 for c in text if c.isupper())  # Count of uppercase letters
    stats['lowercase'] = sum(1 for c in text if c.islower())  # Count of lowercase letters
    stats['digits'] = sum(1 for c in text if c.isdigit())  # Count of digits
    return stats

# Function to filter products based on price range and category
def filter_products(products, min_price=0, max_price=1000, category=None):
    filtered = []
    for p in products:  # Iterate through the list of products
        if p['price'] >= min_price and p['price'] <= max_price:  # Check price range
            if category is None or p['category'] == category:  # Check category if provided
                filtered.append(p)  # Add product to the filtered list
    return filtered

# Function to generate a report from data
def generate_report(data, output_file=None):
    report = []
    report.append(f"Report generated on: {datetime.now()}")  # Add timestamp to the report
    report.append(f"Total items: {len(data)}")  # Add total item count
    
    # Check if the first item in data is a dictionary to extract column names
    if isinstance(data[0], dict):
        keys = data[0].keys()
        report.append("\nColumns: " + ", ".join(keys))  # Add column names to the report
    
    # Write the report to a file if output_file is provided
    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(report))
    return "\n".join(report)  # Return the report as a string

# Function to calculate basic statistics from a list of numbers
def calculate_stats(numbers):
    if not numbers:  # Handle empty list case
        return None
    
    stats = {}
    stats['mean'] = sum(numbers) / len(numbers)  # Calculate mean
    stats['min'] = min(numbers)  # Find minimum value
    stats['max'] = max(numbers)  # Find maximum value
    stats['range'] = stats['max'] - stats['min']  # Calculate range
    
    sorted_nums = sorted(numbers)  # Sort the numbers
    mid = len(sorted_nums) // 2
    stats['median'] = (sorted_nums[mid] + sorted_nums[~mid]) / 2  # Calculate median
    
    return stats

# Function to process user input and perform actions based on commands
def process_user_input(input_str):
    try:
        if input_str.lower() == 'exit':  # Exit command
            return False
        elif input_str.startswith('calc '):  # Calculate command
            expr = input_str[5:]  # Extract the expression
            return eval(expr)  # Evaluate the expression (SECURITY RISK)
        elif input_str.startswith('repeat '):  # Repeat command
            text, times = input_str[7:].split(maxsplit=1)  # Extract text and repetition count
            return text * int(times)  # Repeat the text
        else:
            return input_str.upper()  # Default: Convert input to uppercase
    except:  # Bare except block (BAD PRACTICE)
        return "Invalid input"

# Main block to test the functions
if __name__ == "__main__":
    from datetime import datetime  # Import moved here (should be at the top)
    
    sample_text = "Hello World! 123"
    print(analyze_text(sample_text))  # Test analyze_text function
    
    products = [
        {'name': 'A', 'price': 100, 'category': 'X'},
        {'name': 'B', 'price': 200, 'category': 'Y'},
    ]
    print(filter_products(products, 150, 250))  # Test filter_products function
    
    print(generate_report(products))  # Test generate_report function
    
    numbers = [1, 2, 3, 4, 5]
    print(calculate_stats(numbers))  # Test calculate_stats function
    
    print(process_user_input("calc 5+3"))  # Test process_user_input with calc command
    print(process_user_input("repeat abc 3"))  # Test process_user_input with repeat command
```