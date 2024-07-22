# program to print the following star pattern
#   *
#  ***
# *****
n=3 #number of rows(n) 
b=3 #number of spaces (b)
i=1 
for c in range(i,n+1):
    print(f"{"  "*b}{" *"*i}")
    i=i+2 #number of stars(i) increases by 2 in each iteration
    b=b-1 #number of spaces(b) decreases by 1 in each iteration

