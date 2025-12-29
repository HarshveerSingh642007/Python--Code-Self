# Factorial calculation using a while loop

print("=== FACTORIAL USING WHILE LOOP ===")

num = int(input("Enter number: "))
fact = 1
i = 1

print(num, "! calculation:")
while i <= num:
    fact = fact * i
    print(i, end=" * " if i < num else " = ")
    i = i + 1

print(fact)
input("Press Enter to close...")
