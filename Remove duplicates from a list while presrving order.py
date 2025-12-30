# Remove duplicates from a list while preserving order

lst = [1, 2, 2, 3, 1, 4]
new_lst = []

for item in lst:
    if item not in new_lst:
        new_lst.append(item)

print("No duplicates:", new_lst)
input()
