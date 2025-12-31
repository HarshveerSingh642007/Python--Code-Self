# Separate a list of numbers into even and odd lists

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("Evens:", evens)
print("Odds :", odds)
input()
