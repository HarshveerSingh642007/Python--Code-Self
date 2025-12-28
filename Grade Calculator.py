#Grade Calculator

print("=== Grade Calculator ===")

total = float(input("Enter total marks: "))
marks = float(input("Enter your marks: "))

percentage = (marks / total) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "F"

print("Percentage:", percentage)
print("Grade:", grade)
input("Press Enter...")
