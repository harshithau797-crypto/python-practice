numbers = [4, 2, 7, 4, 2, 9, 7, 1]
unique = []
for num in numbers:
 if num not in unique:
    unique.append(num)
print(unique)