# while loop statement

# program to print first 10 even numbers
i=0
# while loop continues to iterate until the condition is false
while(i<=10): 
    if(i%2==0):
     print(i)
    i+=1 #increment the value by 1
print("--------------------------------------------")
# program to print first 10 integers and their square
count=1
while(count<=10):
   print(f"The square of {count} = {count**2}")
   count+=1  
print("--------------------------------------------")
# program to take user input numbers only less than 50
# else with while loop
i=int(input("Enter the number :"))
while(i<=50):
   print(i)
   i=int(input("Enter the number :"))
else:
   print("the number is greater than 50")
