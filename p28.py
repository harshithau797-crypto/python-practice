numbers = [10, 20, 30, 40, 50, 60]
total=0
for num in numbers:
    total+=num
    average=total/len(numbers)
    count=0
for num in numbers:
    if num>average:
        count+=1
print(average)        
print(count)        