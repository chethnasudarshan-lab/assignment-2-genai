# Question 1: Personal Bio Card
# This program displays student details in a formatted box layout.

# Variable definitions
student_name = "John Doe"
student_age = 20
course_name = "Python Programming"
college_name = "ABC University"
email_address = "john@example.com"

# Printing the formatted bio card
print("╔════════════════════════════════╗")
print("║       STUDENT BIO CARD         ║")
print("╠════════════════════════════════╣")
print(f"║ Name    : {student_name:<20} ║")
print(f"║ Age     : {student_age} years{' ' * 11}║")
print(f"║ Course  : {course_name:<20} ║")
print(f"║ College : {college_name:<20} ║")
print(f"║ Email   : {email_address:<20} ║")
print("╚════════════════════════════════╝")