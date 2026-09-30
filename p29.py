numbers = [23, 67, 12, 89, 45, 34, 90, 56]

largest = numbers[0]

for num in numbers:
    if num>largest:
        largest=num

print(largest)