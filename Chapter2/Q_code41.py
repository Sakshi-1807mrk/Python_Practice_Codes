# program to find whether given number is prime or not

num=int(input("Enter the Number : "))
if(num<=1):
  print(f"{num} is not prime number ")
else:
# num**0.5 calculates the square root of num.
# int(num**0.5) converts the result to integer.(round up the dec no.)
# +1 adds 1 to the result, to include the square root in the range.
 for i in range(2,int(num**0.5)+1):
  if(num%i!=0):# if remainder not equal to 0 then the number is prime
   print(f"{num} is prime number")
   break
  else:print(f"{num} is not prime number")
  break

   
