# This is my Calculator project for CODSOFT Internship programme

import time
print("Welcome to Einstein-Calc!")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    time.sleep(2)
    print("\nOperation Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    prompt = input(">> Select an operation(1/2/3/4/5): ")

    if prompt == "1":
        time.sleep(0.3)
        print("\n>>>>> Addition <<<<<")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        result = add(firstNumber, secondNumber)
        print(f">> Result: {firstNumber} + {secondNumber} = {result}")
        continue

    elif prompt == "2":
        time.sleep(0.3)
        print("\n>>>>> Subtraction <<<<<")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        result = subtract(firstNumber, secondNumber)
        print(f"\nResult: {firstNumber} - {secondNumber} = {result}")
        continue

    elif prompt == "3":
        time.sleep(0.3)
        print("\n>>>>> Multiply <<<<<")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        result = multiply(firstNumber, secondNumber)
        print(f"\nResult: {firstNumber} * {secondNumber} = {result}")
        continue

    elif prompt == "4":
        time.sleep(0.3)
        print("\n>>>>> Divide <<<<<")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        if secondNumber == 0:
            print("Error: cannot divide by zero")
        else:
            result = divide(firstNumber, secondNumber)
            print(f"\nResult: {firstNumber} / {secondNumber} = {result}")
        continue

    elif prompt == '5':
        time.sleep(1)
        print("Exiting application.......")
        break
    else:
        print("Invalid input")
        continue
