# Question 4: Age Calculator
# This program calculates age details based on birth year.

from datetime import datetime

try:
    # Taking birth year from user
    birth_year = int(input("Enter your birth year: "))

    # Get current year
    current_year = datetime.now().year

    # Check if birth year is valid
    if birth_year > current_year:
        print("Birth year cannot be in the future.")
    else:
        age = current_year - birth_year
        age_in_months = age * 12
        age_in_days = age * 365
        age_in_hours = age_in_days * 24
        age_in_minutes = age_in_hours * 60
        years_until_100 = 100 - age

        print("\n--- Age Details ---")
        print("Current Age:", age)
        print("Age in Months:", age_in_months)
        print("Age in Days (approx):", age_in_days)
        print("Age in Hours:", age_in_hours)
        print("Age in Minutes:", age_in_minutes)

        if years_until_100 > 0:
            print("Years until 100:", years_until_100)
        else:
            print("You are already 100 or older!")

except ValueError:
    print("Invalid input. Please enter a valid year.")