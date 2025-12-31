# Replace negative numbers in a list with zero

lst = [1, -2, 3, -4, 5, -6]
print("Original:", lst)

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print("After replace:", lst)
input()
