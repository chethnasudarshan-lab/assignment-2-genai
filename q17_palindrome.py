# Question 17: Palindrome Checker
# This program checks whether a word is a palindrome.

print("--- Palindrome Checker ---")

word = input("Enter a word: ")

reversed_word = ""  # this will store the reversed word

# reverse the word one letter at a time
for ch in word:
    reversed_word = ch + reversed_word

# compare original word and reversed word
if word == reversed_word:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")