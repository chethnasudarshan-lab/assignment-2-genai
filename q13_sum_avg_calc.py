# Question 13: Sum and Average Calculator
# This program finds the sum and average of 5 numbers entered by the user.

print("--- Sum and Average Calculator ---")

total = 0  # starting total as 0

# taking 5 numbers from the user
for i in range(1, 6):
    number = float(input("Enter number " + str(i) + ": "))
    total = total + number  # adding each number to total

# finding average
average = total / 5

# printing the results
print("The total is:", total)
print("The average is:", average)