# Question 14: Factorial Calculator
# This program calculates the factorial of a number.

print("--- Factorial Calculator ---")

number = int(input("Enter a number: "))

factorial = 1  # starting value is 1

# multiply numbers from 1 to the given number
for i in range(1, number + 1):
    factorial = factorial * i

# print the result
print("Factorial of", number, "is", factorial)