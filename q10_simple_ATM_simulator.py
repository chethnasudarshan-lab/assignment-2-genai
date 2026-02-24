# Question 10: Simple ATM Simulator
# This program simulates basic ATM operations.

print("--- ATM Simulator ---")  # Display title

balance = 5000  # Initial balance

# Show menu options
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = input("Enter your choice: ")  # Take user choice

# If user wants to check balance
if choice == "1":
    print("Your balance is:", balance)

# If user wants to deposit money
elif choice == "2":
    amount = float(input("Enter amount to deposit: "))
    balance = balance + amount  # Add amount to balance
    print("Updated balance is:", balance)

# If user wants to withdraw money
elif choice == "3":
    amount = float(input("Enter amount to withdraw: "))
    
    # Check if sufficient balance is available
    if amount <= balance:
        balance = balance - amount  # Deduct money
        print("Updated balance is:", balance)
    else:
        print("Insufficient balance.")

# If user enters invalid option
else:
    print("Invalid choice.")