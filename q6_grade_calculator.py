# Question 6: Grade Calculator
# This program calculates total marks, percentage,
# grade and whether the student passed or failed.

total_marks = 0
passed_all_subjects = True

print("--- Grade Calculator ---")

for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + ": "))

    if mark < 0 or mark > 100:
        print("Marks should be between 0 and 100.")
        passed_all_subjects = False

    total_marks = total_marks + mark

    if mark < 40:
        passed_all_subjects = False

percentage = (total_marks / 500) * 100

# Finding grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Pass or Fail
if passed_all_subjects:
    result = "Pass"
else:
    result = "Fail"

print("\n--- RESULT ---")
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)