# Question 8: Number Guessing Game
# This program asks the user to guess a number.

import random

print("--- Number Guessing Game ---")

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
elif guess < secret_number:
    print("Too low! The correct number was", secret_number)
else:
    print("Too high! The correct number was", secret_number)