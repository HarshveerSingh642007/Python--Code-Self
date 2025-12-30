# Find the position of a number in a list

lst = [10, 20, 30, 40, 50]
find_num = 30
position = -1

for i in range(len(lst)):
    if lst[i] == find_num:
        position = i
        break

if position != -1:
    print(find_num, "found at index", position)
else:
    print(find_num, "not in list")

input()
