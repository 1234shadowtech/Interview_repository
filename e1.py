def analyze_text(text):
    stats = {}
    stats['length'] = len(text)
    stats['words'] = len(text.split())
    stats['uppercase'] = sum(1 for c in text if c.isupper())
    stats['lowercase'] = sum(1 for c in text if c.islower())
    stats['digits'] = sum(1 for c in text if c.isdigit())
    return stats

def filter_products(products, min_price=0, max_price=1000, category=None):
    filtered = []
    for p in products:
        if p['price'] >= min_price and p['price'] <= max_price:
            if category is None or p['category'] == category:
                filtered.append(p)
    return filtered

def generate_report(data, output_file=None):
    report = []
    report.append(f"Report generated on: {datetime.now()}")
    report.append(f"Total items: {len(data)}")
    
    if isinstance(data[0], dict):
        keys = data[0].keys()
        report.append("\nColumns: " + ", ".join(keys))
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(report))
    return "\n".join(report)

def calculate_stats(numbers):
    if not numbers:
        return None
    
    stats = {}
    stats['mean'] = sum(numbers) / len(numbers)
    stats['min'] = min(numbers)
    stats['max'] = max(numbers)
    stats['range'] = stats['max'] - stats['min']
    
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2
    stats['median'] = (sorted_nums[mid] + sorted_nums[~mid]) / 2
    
    return stats

def process_user_input(input_str):
    try:
        if input_str.lower() == 'exit':
            return False
        elif input_str.startswith('calc '):
            expr = input_str[5:]
            return eval(expr)
        elif input_str.startswith('repeat '):
            text, times = input_str[7:].split(maxsplit=1)
            return text * int(times)
        else:
            return input_str.upper()
    except:
        return "Invalid input"

if __name__ == "__main__":
    from datetime import datetime
    
    sample_text = "Hello World! 123"
    print(analyze_text(sample_text))
    
    products = [
        {'name': 'A', 'price': 100, 'category': 'X'},
        {'name': 'B', 'price': 200, 'category': 'Y'},
    ]
    print(filter_products(products, 150, 250))
    
    print(generate_report(products))
    
    numbers = [1, 2, 3, 4, 5]
    print(calculate_stats(numbers))
    
    print(process_user_input("calc 5+3"))
    print(process_user_input("repeat abc 3"))
