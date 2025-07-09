```python
# Function to analyze text and return statistics
def analyze_text(text: str) -> dict:  # Added type hints
    stats = {}
    stats['length'] = len(text)  # Total length of the text
    stats['words'] = len(text.split())  # Number of words in the text
    stats['uppercase'] = sum(1 for c in text if c.isupper())  # Count of uppercase letters
    stats['lowercase'] = sum(1 for c in text if c.islower())  # Count of lowercase letters
    stats['digits'] = sum(1 for c in text if c.isdigit())  # Count of digits
    return stats

# Function to filter products based on price range and category
def filter_products(products: list, min_price: int = 0, max_price: int = 1000, category: str = None) -> list:  # Added type hints
    # Use list comprehension for better readability and performance
    return [
        p for p in products
        if p['price'] >= min_price and p['price'] <= max_price and (category is None or p['category'] == category)
    ]

# Function to generate a report from data
def generate_report(data: list, output_file: str = None) -> str:  # Added type hints
    from datetime import datetime  # Import should be moved to the top of the file
    report = []
    report.append(f"Report generated on: {datetime.now()}")  # Add timestamp
    report.append(f"Total items: {len(data)}")  # Add total item count
    
    # Check if data contains dictionaries and extract keys
    if data and isinstance(data[0], dict):  # Added check for empty data
        keys = data[0].keys()
        report.append("\nColumns: " + ", ".join(keys))  # Add column names
    
    # Write report to file if output_file is provided
    if output_file:
        try:
            with open(output_file, 'w') as f:
                f.write("\n".join(report))
        except IOError as e:  # Added error handling for file operations
            return f"Error writing to file: {e}"
    return "\n".join(report)

# Function to calculate basic statistics from a list of numbers
def calculate_stats(numbers: list) -> dict:  # Added type hints
    if not numbers:  # Handle empty list
        return None
    
    # Validate input to ensure all elements are numeric
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements in the list must be numeric")
    
    stats = {}
    stats['mean'] = sum(numbers) / len(numbers)  # Calculate mean
    stats['min'] = min(numbers)  # Find minimum value
    stats['max'] = max(numbers)  # Find maximum value
    stats['range'] = stats['max'] - stats['min']  # Calculate range
    
    # Calculate median
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2
    stats['median'] = (sorted_nums[mid] + sorted_nums[~mid]) / 2  # Handle even/odd cases
    
    return stats

# Function to process user input and perform actions
def process_user_input(input_str: str) -> any:  # Added type hints
    try:
        if input_str.lower() == 'exit':  # Exit command
            return False
        elif input_str.startswith('calc '):  # Evaluate mathematical expression
            expr = input_str[5:]
            # Replace eval with a safer alternative
            import ast
            import operator as op

            # Define supported operators
            allowed_operators = {
                ast.Add: op.add,
                ast.Sub: op.sub,
                ast.Mult: op.mul,
                ast.Div: op.truediv,
                ast.Pow: op.pow,
                ast.BitXor: op.xor,
            }

            def eval_expr(expr):
                node = ast.parse(expr, mode='eval').body
                if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
                    return allowed_operators[type(node.op)](eval_expr(node.left), eval_expr(node.right))
                elif isinstance(node, ast.Num):
                    return node.n
                else:
                    raise ValueError("Unsupported expression")

            return eval_expr(expr)  # Safer evaluation
        elif input_str.startswith('repeat '):  # Repeat text multiple times
            try:
                text, times = input_str[7:].split(maxsplit=1)
                return text * int(times)
            except ValueError:  # Handle invalid input
                return "Invalid repeat command"
        else:
            return input_str.upper()  # Convert input to uppercase
    except Exception as e:  # Replace bare except with specific exception handling
        return f"Error processing input: {e}"  # Provide more descriptive error messages

# Main block to test the functions
if __name__ == "__main__":
    from datetime import datetime  # Import should be moved to the top of the file
    
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
    print(process_user_input("calc 5+3"))  # SECURITY RISK: eval usage replaced
    print(process_user_input("repeat abc 3"))
```