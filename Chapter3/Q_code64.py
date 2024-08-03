#  recursion in python

# default value of the times the recursive function can call itself infinitly
import sys
print(sys.getrecursionlimit())

# how to set infinite recursive function limit
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())
print("-----------------------------------")
# recursion example

def greet(n):
    if(n<=5):
        print('hello')
        greet(n+1)
greet(1)
print("-----------------------------------")
# recursion for factorial
def factorial(n):
    # base condition
    if(n==1):
        return 1
    return n*factorial(n-1)#funnction calls itself again
num=int(input("Enter the num : "))
print(f"The factorial of {num} is {factorial(num)}")
print("-----------------------------------")
# recursion for fibonachi series
def fibonacci(num):
     if(num==0):
      return 0
     elif(num==1):
      return 1
     else:
      return fibonacci(num-1) + fibonacci(num-2)
num=int(input("Enter the num : "))
print(f"The fibonacci number for {num} is : {fibonacci(num)} ")
print('---------------------------------------')

# fibonacci series using recursion
def fib(num, prev1=0, prev2=1):
    if num <= 1:
        return prev1
    else:
        fn = fib(num-1, prev2, prev1+prev2)
        print(fn, end=" ")
        return fn

num = int(input("Enter the num: "))
fib(num)


