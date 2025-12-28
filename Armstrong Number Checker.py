# Armstrong Number Checker

print("=== ARMSTRONG NUMBER CHECKER ===")

num = int(input("Enter a number: "))
original = num
total = 0
digits = len(str(original))

print("Digits:", digits)

while num > 0:
    digit = num % 10
    total = total + (digit ** digits)
    num = num // 10

print("Original:", original)
print("Sum of powers:", total)

if total == original:
    print(original, "is ARMSTRONG NUMBER!")
else:
    print(original, "is NOT armstrong")

input("Press Enter to close...")
