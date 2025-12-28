# Palindrome Number Checker

print("=== PALINDROME NUMBER CHECKER ===")

num = int(input("Enter a number: "))
original = num
reverse = 0

print("Checking if", num, "is palindrome...")

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Original:", original)
print("Reversed:", reverse)

if original == reverse:
    print(num, "is PALINDROME NUMBER!")
else:
    print(num, "is NOT palindrome")

input("Press Enter to close...")
