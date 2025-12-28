# BMI Calculator

print("=== BMI Calculator ===")

weight = float(input("Weight in kg: "))
height = float(input("Height in meters: "))

bmi = weight / (height * height)

print("Your BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

input("Press Enter...")
