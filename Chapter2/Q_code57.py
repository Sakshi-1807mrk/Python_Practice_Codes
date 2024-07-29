# return statement in functions

# with no return value
def average(a,b):
    avg=(a+b)/2
c=average(6,7)
print(c) # will print none as no return statement mention

# with return value 
def average(a,b):
    avg=(a+b)/2
    return avg
c=average(6,7)
print(c) 
