# Question 2: Simple Calculator
# This program asks the user for two numbers and performs
# addition, subtraction, multiplication, division,
# modulus and exponentiation.

try:
    # Taking input from the user
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    print("\nResults:")

    # Addition
    print(f"{first_number} + {second_number} = {first_number + second_number}")

    # Subtraction
    print(f"{first_number} - {second_number} = {first_number - second_number}")

    # Multiplication
    print(f"{first_number} * {second_number} = {first_number * second_number}")

    # Division and Modulus (check for zero)
    if second_number != 0:
        print(f"{first_number} / {second_number} = {first_number / second_number}")
        print(f"{first_number} % {second_number} = {first_number % second_number}")
    else:
        print("Division by zero is not allowed.")
        print("Modulus by zero is not allowed.")

    # Exponentiation
    print(f"{first_number} ** {second_number} = {first_number ** second_number}")

except ValueError:
    print("Invalid input. Please enter numeric values only.")