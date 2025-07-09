```python
def greet(name):  # Define a function to greet a user by name
    return f"Hello, {name}!"  # Return a formatted greeting string

def add(a, b):  # Define a function to add two numbers
    return a + b  # Return the sum of the two numbers

def main():  # Define the main function to execute the program logic
    print(greet("Alice"))  # Call the greet function with "Alice" and print the result
    print("Sum:", add(3, 4))  # Call the add function with 3 and 4, and print the result

if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function
```