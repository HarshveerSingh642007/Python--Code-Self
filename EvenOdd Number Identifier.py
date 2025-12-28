#Even / Odd Number Identifier

print("=== Even or Odd? ===")

while True:
    num = int(input("Enter number (0 to quit): "))
    
    if num == 0:
        break
        
    if num % 2 == 0:
        print(num, "is EVEN")
    else:
        print(num, "is ODD")

print("Thanks!")
input("Press Enter...")
