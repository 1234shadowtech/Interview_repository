```python
# Function to analyze text and return statistics
def analyze_text(text):
    stats = {}  # Dictionary to store text statistics
    stats['length'] = len(text)  # Total length of the text
    stats['words'] = len(text.split())  # Number of words in the text
    stats['uppercase'] = sum(1 for c in text if c.isupper())  # Count of uppercase letters
    stats['lowercase'] = sum(1 for c in text if c.islower())  # Count of lowercase letters
    stats['digits'] = sum(1 for c in text if c.isdigit())  # Count of digits
    return stats

# Function to filter products based on price range and category
def filter_products(products, min_price=0, max_price=1000, category=None):
    filtered = []  # List to store filtered products
    for p in products:
        # Check if product price is within the range and matches the category (if provided)
        if p['price'] >= min_price and p['price'] <= max_price:
            if category is None or p['category'] == category:
                filtered.append(p)
    return filtered

# Function to generate a report from data and optionally write to a file
def generate_report(data, output_file=None):
    report = []  # List to store report lines
    report.append(f"Report generated on: {datetime.now()}")  # Add timestamp to the report
    report.append(f"Total items: {len(data)}")  # Add total item count
    
    # Check if data contains dictionaries and list their keys as columns
    if isinstance(data[0], dict):
        keys = data[0].keys()
        report.append("\nColumns: " + ", ".join(keys))
    
    # Write the report to a file if an output file is specified
    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(report))
    return "\n".join(report)

# Function to calculate statistics for a list of numbers
def calculate_stats(numbers):
    if not numbers:  # Return None if the list is empty
        return None
    
    stats = {}  # Dictionary to store statistics
    stats['mean'] = sum(numbers) / len(numbers)  # Calculate mean
    stats['min'] = min(numbers)  # Find minimum value
    stats['max'] = max(numbers)  # Find maximum value
    stats['range'] = stats['max'] - stats['min']  # Calculate range
    
    sorted_nums = sorted(numbers)  # Sort numbers for median calculation
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
            return eval(expr)  # Evaluate the expression (Security Risk)
        elif input_str.startswith('repeat '):  # Repeat command
            text, times = input_str[7:].split(maxsplit=1)  # Extract text and repetition count
            return text * int(times)  # Repeat the text
        else:
            return input_str.upper()  # Default: Convert input to uppercase
    except:  # Bare except block (Bad Practice)
        return "Invalid input"

# Main block to test the functions
if __name__ == "__main__":
    from datetime import datetime  # Import datetime module (should be at the top)
    
    # Test analyze_text function
    sample_text = "Hello World! 123"
    print(analyze_text(sample_text))
    
    # Test filter_products function
    products = [
        {'name': 'A', 'price': 100, 'category': 'X'},
        {'name': 'B', 'price': 200, 'category': 'Y'},
    ]
    print(filter_products(products, 150, 250))
    
    # Test generate_report function
    print(generate_report(products))
    
    # Test calculate_stats function
    numbers = [1, 2, 3, 4, 5]
    print(calculate_stats(numbers))
    
    # Test process_user_input function
    print(process_user_input("calc 5+3"))
    print(process_user_input("repeat abc 3"))
```