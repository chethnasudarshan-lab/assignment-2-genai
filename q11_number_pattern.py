# Question 11: Number Pattern Printer
# This program prints a simple number pattern.

print("--- Number Pattern ---")

# Ask user how many rows they want
rows = int(input("Enter number of rows: "))

# This loop runs for each row
for i in range(1, rows + 1):

    # This loop prints numbers from 1 up to current row number
    for j in range(1, i + 1):
        print(j, end=" ")  # Print numbers in the same line

    # After printing one row, move to next line
    print()