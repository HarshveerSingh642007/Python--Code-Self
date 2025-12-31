# Find common elements between two lists by iterating through one list and checking for membership in the other

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common numbers:", common)
input()
