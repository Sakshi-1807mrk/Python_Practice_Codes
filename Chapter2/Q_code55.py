# 1) program to check if a list contains a palindrome (ex:refer,12321 )of elements.
list=['eye','force','pressure','12321','speed']
print(list)
palindrome=False
# Initialize palindrome to False (no palindrome found yet) 
# helps evaluate else condition if no palindrome found
for i in list:
    # # Check if the characters in string is equal to its reverse
    if(i[0]==i[-1] and i[1]==i[-2] and i[2]==i[-3]):
     palindrome=True
    #Initialize palindrome to True if found so if condition can be evaluated    
if(palindrome):
    print("list contains a palindrome")
else:
    print("list does not contains palindrome")
print('-----------------------------------------------')
# 2)program to sum a list with four numbers
num_list=[]
sum=0
n=int(input('Enter the Number of elements :'))
for i in range(n):
#append() for adding elements to the end of list
   num_list.append(int(input(f'Enter the number for {i} :')))
   sum+=num_list[i]
print("list :",num_list)
print('The sum of list is :',sum)