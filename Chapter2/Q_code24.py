# nested if 

num=int(input("Enter the number:"))
if(num>0):
    print("Number is positive")
    if(num>0 and num<10):
        print("Number is between 0-10")
    elif(num>10 and num<50):
        print("Number is between 10-50")
    else:
        print("Number is between 50-100")
elif(num<0):
    print("Number is negative")
else:
    print("Number is zero")