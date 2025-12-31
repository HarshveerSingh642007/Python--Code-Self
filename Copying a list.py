# Create a copy of a list by iterating through each element and appending it to a new list 

original = [1, 2, 3, 4]
copy_list = []

for item in original:
    copy_list.append(item)

print("Original:", original)
print("Copy   :", copy_list)
input()
