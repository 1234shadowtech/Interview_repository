def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return None
def sqrt(a):
    return a**0.5
def main():
    x = 10
    y = 5
    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    print(sqrt(x))

main()
