# Reverse a list without using build -in functions

lst = [10, 20, 30, 40]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Original:", lst)
print("Reverse :", rev)
input()
