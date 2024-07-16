#  Explicit typecasting

string="5"
number = 7
string_number= int(string)
sum=number + string_number
print("The sum of numbers is:",sum)

# Implicit typecasting

a = 4.5
b = 3
c=a+b # it automatically coverts c in float as it is float addition
print(type(c)) 
print("The sum of numbers is:",c)