num=int(input("Enter Number: "))
if 100<=num<=999:
    a=num%10
    b=num//10%10
    c=num//100
    print(a+b+c)
else:print("Error,not 3 digit number")







