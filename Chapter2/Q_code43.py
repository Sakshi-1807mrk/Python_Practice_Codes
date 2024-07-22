#  program to print the factorial of given number
i=1
factorial=1
n=int(input("Enter the Number :")) 
for i in range(i,n+1):#loop from i to n
    factorial=factorial*i 
# multiply the current value of i for every iteration and store it in factorial variable
print(f"Factorial of {n} is {factorial}")