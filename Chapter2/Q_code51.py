# 1)program using functions to find the greatest of three numbers

def greatest(a,b,c):
     if(a>=b and a>=c):# >= so that function can handle two or more same numbers
        print(f"{a} is greatest number")
     elif(b>=a and b>=c):
        print(f"{b} is greatest number")
     else:
        print(f"{c} is greatest number")
a=int(input("Enter first num  :"))
b=int(input("Enter second num :"))
c=int(input("Enter third num  :"))
greatest(a,b,c)
print('------------------------------------------')

                                                             