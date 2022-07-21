# write a programe to accept month from user and display how many days it has 
month=int(input("Enter month"))
if month<=12 and month>0:
    if month==2:
        print("this month has 28/29 days")
    elif month==7 or month==12:
        print("this month has 31 days")
    elif month<=7:
        if month%2==0:
            print('this is month has 30 days')
        elif month%2!=0:
            print('this month has 31 days')
    elif month>7:
        if month%2!=0:
            print('this is month has 30 days')
        elif month%2==0:
            print('this month has 31 days')
    else:
        print('this invalid month')
else:
    print("invalid month")