# Question 9: Ticket Pricing System
# This program calculates ticket price based on age.

print("--- Ticket Pricing ---")  # Display title

age = int(input("Enter your age: "))  # Take age input

# Check age conditions one by one
if age < 5:
    price = 0  # Free ticket for small children

elif age <= 18:
    price = 100  # Discount price for children/teens

elif age <= 60:
    price = 200  # Regular adult price

else:
    price = 150  # Senior citizen price

print("Your ticket price is:", price)  # Display final price