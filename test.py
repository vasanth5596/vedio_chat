def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# User input functions

def main():
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        operation = input('Enter operation (+ or -): ')

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        else:
            print('Invalid operation')
            return
        print(f'Result: {result}')
    except ValueError:
        print('Invalid input, please enter numeric values')

if __name__ == '__main__':
    main()