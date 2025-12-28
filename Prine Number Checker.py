# Prine Number Checker

num = int(input("Enter number to check prime: "))

is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if num <= 1:
    print(num, "is not prime")
elif is_prime:
    print(num, "is PRIME")
else:
    print(num, "is not prime")

input("Press Enter...")
