# docstring in python
# using docstring in program
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

# print the docstring using doc attribute
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)