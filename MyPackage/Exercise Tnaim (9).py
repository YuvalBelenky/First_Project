from random import randint
day=int(input("Enter Day: "))
month=int(input("Enter Month: "))
year=int(input("Enter Year: "))
if 1<=day<=31 and 1<=month<=12 and 1950<=year<=2020:
    right=year%10
    middle=year//10%10
    if 1<=day<=9:
        day=str(day)
        day="0"+day
        if 1<=month<=9:
           month=str(month)
        month="0"+month
print(f"{day}/{month}/{middle}{right}")








