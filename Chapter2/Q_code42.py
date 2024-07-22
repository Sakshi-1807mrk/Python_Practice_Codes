# a program to find the sum of first n natural numbers using for and while loop
# using for loop
n=int(input("Enter the Number :")) 
i=1
sum=0
for i in range(i,n+1):
 sum = sum+i
print(f"The sum of {n} natural numbers is {sum}")
print("---------------------------------------------")
# using while loop
n=int(input("Enter the Number :")) 
i=1
sum=0
while(i<=n):
  sum=sum+i
  i=i+1
print(f"The sum of {n} natural numbers is {sum}")
