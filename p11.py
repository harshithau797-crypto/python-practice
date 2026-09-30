unit=int(input("Enter no. of units:"))
if unit<=100 :
    res=unit*5
    print("Units:",res)
elif unit<=200 :   
    res=(100*5)+((unit-100)*7)
    print("Units:",res)
else:
    res=(100*5)+(100*7)+((unit-200)*10)
    print("Units:",res)
