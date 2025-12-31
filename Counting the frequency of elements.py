# Counting the frequency of elements in a list

lst = [1, 2, 2, 3, 1, 1, 4]
counts = {}

for num in lst:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1

print("Frequency:")
for key, value in counts.items():
    print(key, ":", value)

input()
