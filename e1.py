def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return 3.14159 * radius * radius
    elif shape == "rectangle":
        length, width = args
        return length * width
    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height
    else:
        return None

def process_data(data):
    result = []
    for item in data:
        if isinstance(item, int):
            if item % 2 == 0:
                result.append(item * 2)
            else:
                result.append(item * 3)
        elif isinstance(item, str):
            result.append(item.upper())
    return result

def validate_user(username, password):
    if len(username) < 4:
        return False
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True

def format_output(data, format_type):
    if format_type == "json":
        import json
        return json.dumps(data)
    elif format_type == "csv":
        import csv
        import io
        output = io.StringIO()
        writer = csv.writer(output)
        for row in data:
            writer.writerow(row)
        return output.getvalue()
    else:
        return str(data)

def main():
    print(calculate_area("circle", 5))
    print(calculate_area("rectangle", 4, 7))
    print(process_data([1, 2, 3, "hello"]))
    print(validate_user("admin", "Password123"))
    print(format_output([["a", "b"], ["c", "d"]], "csv"))

if __name__ == "__main__":
    main()
