# Simple calculator program

name = input("Hey, what's your name? ")
print("Hi " + name + "! Let's do some math.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")

choice = input("Pick 1-4: ")

if choice == '1':
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif choice == '2':
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif choice == '3':
    result = num1 * num2
    print(num1, "x", num2, "=", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(num1, "÷", num2, "=", result)
    else:
        print("Can't divide by zero bro!")
else:
    print("Wrong choice, try again.")

input("Press Enter to close...")
