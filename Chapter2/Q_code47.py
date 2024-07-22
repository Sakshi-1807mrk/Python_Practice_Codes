# program to print multiplication table of n using for loop in reversed order
a=int(input("Enter the Number :"))
b=10
for i in range(b):
    print(f"{a} x {b} = {a*b}")
    b=b-1 #decrements the value by 1
