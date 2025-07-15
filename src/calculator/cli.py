import operations


def main():
    print("Choose operation: add, subtract, multiply, divide, power, modulus")
    op = input("Operation: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == "add":
        result = operations.add(a, b)
    elif op == "subtract":
        result = operations.subtract(a, b)
    elif op == "multiply":
        result = operations.multiply(a, b)
    elif op == "divide":
        result = operations.divide(a, b)
    elif op == "power":
        result = operations.power(a, b)
    elif op == "modulus":
        result = operations.modulus(a, b)
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")


main()
