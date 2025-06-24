# Frozen version of the test script

"""This script performs basic calculator operations to test deployment."""

def main():
    print("Frozen Test Calculator")
    num1 = 10  # Example first number
    num2 = 5   # Example second number
    operator = "+"  # Example operator

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()