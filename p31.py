numbers = [34, 12, 56, 7, 89, 23, 5, 41]
small=numbers[0]
for num in numbers:
    if num<small:
        small=num
print(small)