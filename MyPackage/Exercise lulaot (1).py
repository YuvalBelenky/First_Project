number=int(input("Enter 3 digit number: "))
while 100<=number<=999:
    a=number%10
    b=number//10 % 10
    c=number//100
    print(a+b+c)
while number<100 or number>999:
    print("Error. not a 3 digit number")
    number = int(input("Enter 3 digit number: "))







