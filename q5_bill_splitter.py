# Question 5: Bill Splitter
# This program calculates how to split a restaurant bill among people.

print("--- Bill Splitter ---")

total_bill = float(input("Enter total bill amount: "))
number_of_people = int(input("Enter number of people: "))
tax_percentage = float(input("Enter tax percentage: "))
tip_percentage = float(input("Enter tip percentage: "))

if number_of_people <= 0:
    print("Number of people must be greater than 0.")

elif total_bill < 0 or tax_percentage < 0 or tip_percentage < 0:
    print("Values cannot be negative.")

else:
    # Calculate tax
    tax_amount = total_bill * tax_percentage / 100
    bill_after_tax = total_bill + tax_amount

    # Calculate tip
    tip_amount = bill_after_tax * tip_percentage / 100
    final_total = bill_after_tax + tip_amount

    # Split per person
    amount_per_person = final_total / number_of_people

    print("\n--- BILL DETAILS ---")
    print("Subtotal:", total_bill)
    print("Tax Amount:", tax_amount)
    print("After Tax:", bill_after_tax)
    print("Tip Amount:", tip_amount)
    print("Total Bill:", final_total)
    print("Amount Per Person:", amount_per_person)