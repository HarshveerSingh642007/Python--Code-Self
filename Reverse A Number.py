# Reverse a number entered by the user

print("=== NUMBER REVERSER ===")

num = int(input("Enter number to reverse: "))
original = num
reverse = 0

print("Reversing", num, "...")

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Original:", original)
print("Reversed:", reverse)

input("Press Enter to close...")
