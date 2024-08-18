#fibonacci series using recursion
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibonacci(n-2) + fibonacci(n-1))
n=int(input("Enter the num :"))
for i in range (1,n+1):
   print(fibonacci(i),end=" ")