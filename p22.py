numbers = [12, 45, 7, 45, 23, 89, 12, 67]
largest=numbers[0]
second_largest=numbers[0]

for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
        
    elif num<largest and num>second_largest:
       second_largest=num


print(second_largest)
    