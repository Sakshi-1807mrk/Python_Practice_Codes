#write a python function to print the following pattern for n rows
# ex : n=3
# * * *
# * *
# *
def smily_pattern(n):
    for i in range(n):
        print("😊 "*n)
        n-=1
n= int(input("Enter the number of rows :"))
smily_pattern(n)