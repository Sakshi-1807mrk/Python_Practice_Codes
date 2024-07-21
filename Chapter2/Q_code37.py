# continue statement
#  program to print only even numbers from list 
for i in [2,5,6,7,8,0]:
    if(i%2!=0):
        continue #skips the iteration for if condition
    print(i)
print("------------------------")
# program to print only vowels in a list
string="i saw an aeroplane flying"
x=['a','e','i','o','u']
for i in string :
    if(i not in x): # membership operator
        continue
    print(i) 
print("------------------------")
# program to skip the iteration when if condition is true
weather=["snow", "rain", "sun", "clouds"]
for x in weather:
    if(x=="sun"):
        continue
    print(x)

