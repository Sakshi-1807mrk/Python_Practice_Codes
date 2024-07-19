# Exercise solutions
# if-elif-else condition
# a program to find greatest of four numbers entered by user
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))
num4=int(input("Enter fourth number :"))
if(num1>num2 and num1>num3 and num1>num4):
        print(f"{num1} is greater")
# if all conditions are true then if block is executed
elif(num2>num1 and num2>num3 and num2>num4):
        print(f"{num2} is greater")
# if condition is false and if all conditions are true in elif block is executed
elif(num3>num1 and num3>num2 and num3>num4):
        print(f"{num3} is greater")
# if above conditions are false and if all conditions are true in elif block is executed
# if all the three conditions are false then else block is executed denoting num4 to be greatest
else:
    print(f"{num4} is greater")