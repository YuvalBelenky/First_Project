age=int(input("Enter your age: "))
while age<0 or age>120:
    print("error")
    age=int(input("Enter your age: "))
if 0<=age<=18:
    print("Child")
if 19<=age<=60:
    print("Adult")
if 61<=age<=120:
    print("Senior")










