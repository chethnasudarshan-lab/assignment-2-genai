# Question 3: String Manipulator
# This program asks the user for a sentence and performs different string operations.

# Taking input from user
sentence = input("Enter a sentence: ")

print("\nOriginal:", sentence)

# Total characters including spaces
total_characters = len(sentence)
print("Characters (with spaces):", total_characters)

# Total characters excluding spaces
characters_without_spaces = len(sentence.replace(" ", ""))
print("Characters (without spaces):", characters_without_spaces)

# Splitting sentence into words
words = sentence.split()

# Total words
total_words = len(words)
print("Words:", total_words)

# Uppercase
print("UPPERCASE:", sentence.upper())

# Lowercase
print("lowercase:", sentence.lower())

# Title case
print("Title Case:", sentence.title())

# First and last word (only if words exist)
if total_words > 0:
    first_word = words[0]
    last_word = words[-1]
    print("First word:", first_word)
    print("Last word:", last_word)
else:
    print("First word: None")
    print("Last word: None")

# Reversed sentence
reversed_sentence = sentence[::-1]
print("Reversed:", reversed_sentence)