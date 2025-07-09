```python
# Function to analyze text statistics
def analyze_text(text: str) -> dict:  # Added type hints for clarity
    stats = {}
    stats['length'] = len(text)  # Total length of the text
    stats['words'] = len(text.split())  # Number of words (split by whitespace)
    stats['uppercase'] = sum(1 for c in text if c.isupper())  # Count of uppercase letters
    stats['lowercase'] = sum(1 for c in text if c.islower())  # Count of lowercase letters
    stats['digits'] = sum(1 for c in text if c.isdigit())  # Count of digits
    return stats

# Function to filter products based on price range and category
def filter_products(products: list, min_price: int = 0, max_price: int = 1000, category: str = None) -> list:  # Added type hints
    filtered = []
    for p in products:
        # Check if product price is within range and matches the category (if provided)
        if p['price'] >= min_price and p['price'] <= max_price:
            if category is None or p['category'] == category:
                filtered.append(p)
    return filtered  # Consider using a list comprehension for better readability

# Function to generate a report from data
def generate_report(data: list, output_file: str = None) -> str:  # Added type hints
    report = []
    report.append(f"Report generated on: {datetime.now()}")  # Add timestamp
    report.append(f"Total items: {len(data)}")  # Add total item count
    
    # Check if data contains dictionaries and list their keys as columns
    if data and isinstance(data[0], dict):  # Added check for empty data
        keys = data[0].keys()
        report.append("\nColumns: " + ", ".join(keys))
    
    # Write report to file if output_file is specified
    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(report))
    return "\n".join(report)

# Function to calculate statistics for a list of numbers
def calculate_stats(numbers: list) -> dict:  # Added type hints
    if not numbers:  # Return None if the list is empty
        return None
    
    stats = {}
    stats['mean'] = sum(numbers) / len(numbers)  # Calculate mean
    stats['min'] = min(numbers)  # Find minimum value
    stats['max'] = max(numbers)  # Find maximum value
    stats['range'] = stats['max'] - stats['min']  # Calculate range
    
    sorted_nums = sorted(numbers)  # Sort numbers for median calculation
    mid = len(sorted_nums) // 2
    stats['median'] = (sorted_nums[mid] + sorted_nums[~mid]) / 2  # Calculate median
    return stats

# Function to process user input and perform actions
def process_user_input(input_str: str):  # Added type hints
    try:
        if input_str.lower() == 'exit':  # Exit command
            return False
        elif input_str.startswith('calc '):  # Calculate expression
            expr = input_str[5:]
            return eval(expr)  # WARNING: Security risk, avoid using eval
        elif input_str.startswith('repeat '):  # Repeat text
            text, times = input_str[7:].split(maxsplit=1)
            return text * int(times)  # Repeat text 'times' times
        else:
            return input_str.upper()  # Convert input to uppercase
    except ValueError:  # Specify exception for invalid integer conversion
        return "Invalid input"
    except Exception as e:  # Catch other exceptions and log the error
        return f"Error: {e}"

# Main block to test the functions
if __name__ == "__main__":
    from datetime import datetime  # Import should be at the top of the file
    
    sample_text = "Hello World! 123"
    print(analyze_text(sample_text))  # Analyze sample text
    
    products = [
        {'name': 'A', 'price': 100, 'category': 'X'},
        {'name': 'B', 'price': 200, 'category': 'Y'},
    ]
    print(filter_products(products, 150, 250))  # Filter products by price range
    
    print(generate_report(products))  # Generate a report for products
    
    numbers = [1, 2, 3, 4, 5]
    print(calculate_stats(numbers))  # Calculate statistics for a list of numbers
    
    print(process_user_input("calc 5+3"))  # Process a calculation command
    print(process_user_input("repeat abc 3"))  # Process a repeat command
```