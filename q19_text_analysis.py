# Question 19: Text Analysis
# This program analyzes a sentence entered by the user.

print("--- Text Analysis ---")

text = input("Enter a sentence: ")

# count total characters
characters = len(text)

# count total words by splitting sentence
words = len(text.split())

# count vowels
vowel_count = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowel_count = vowel_count + 1

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowel_count)
print("Text in uppercase:", text.upper())
print("Text in lowercase:", text.lower())