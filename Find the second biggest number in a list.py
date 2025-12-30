# Find the second biggest number in a list 

numbers = [5, 2, 8, 1, 9, 3]
big1 = big2 = -1

for num in numbers:
    if num > big1:
        big2 = big1
        big1 = num
    elif num > big2:
        big2 = num

print("Second biggest:", big2)
input()
