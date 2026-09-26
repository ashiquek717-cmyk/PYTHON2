def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, q to quit")

    while True:
        operation = input("Choose an operation: ").strip()

        if operation.lower() == 'q':
            print("Goodbye!")
            break

        if operation not in {"+", "-", "*", "/"}:
            print("Invalid operation. Please use +, -, *, or /.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print(f"Result: {result}")
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    calculator()
