# Age Group Finder 

print("=== Age Group Finder ===")

name = input("Your name: ")
age = int(input("Your age: "))

if age < 13:
    group = "Kid"
elif age < 20:
    group = "Teenager"
elif age < 60:
    group = "Adult"
else:
    group = "Senior"

print(name, "you are a", group)
input("Press Enter...")
