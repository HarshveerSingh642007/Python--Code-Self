# Temperature Converter: Celsius to Fahrenheit and vice versa 

print("=== Temp Converter ===")
temp = float(input("Enter temperature: "))
unit = input("C or F? ")

if unit.upper() == "C":
    fahrenheit = (temp * 9/5) + 32
    print(temp, "C =", round(fahrenheit, 2), "F")
elif unit.upper() == "F":
    celsius = (temp - 32) * 5/9
    print(temp, "F =", round(celsius, 2), "C")
else:
    print("Use C or F only")

input("Press Enter...")
