# Finding the maximum number in a list

numbers = [7, 2, 9, 1, 5]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum:", max_num)
input()
