# Question 20: Number System Converter
# This program converts a number into binary, octal, and hexadecimal.

print("--- Number System Converter ---")

number = int(input("Enter a number: "))

# converting number to different number systems
binary = format(number, "b")
octal = format(number, "o")
hexadecimal = format(number, "x")

print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)