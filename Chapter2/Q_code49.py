# program to create a function for greeting someone
def greet(a,b):
    print("Hello,",a,b)
greet('Elisha','Fernandes')
print("----------------------------------")
# 4 types of arguments we can define in a function
# default argument
# keyword argument
# required argument
# variable length argument

# program for passing default arguments
# arguments passed while defining a function  
def average(a=5,b=9):
    avg=(a+b)/2
    print("Default Arguments")
    print("average :",avg)
average() # arguments not passed while function call so default arguments are considered
print("----------------------------------")
def average(a=5,b=9):
    avg=(a+b)/2
    print("average :",avg)
average(2,8) # default arguments(5,9) will be replaced by function call arguments (2,8)
print("----------------------------------")

# program for passing keyword arguments
def Rectangle_area(l,b):
    area=l*b
    print("Keyword Arguments")
    print("Area of the Rectangle:",area)
Rectangle_area(l=4,b=5) # arguments passed in key=value pair
# hence arguments are recognized by parameter names
print("----------------------------------")

# program for passing required arguments
def Square_area(side):
    area=side*side
    print("Required Arguments")
    print("Area of a Square :",area)
Square_area(4) #number of arguments match the actual function defination
print("----------------------------------")