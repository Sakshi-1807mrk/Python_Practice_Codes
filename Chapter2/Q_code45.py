# program to print the following star pattern
# *
# ***
# *****
n=3 #number of rows(n)
i=1 #number of stars(i)
for c in range(1,n+1): 
    print(f"{"* "*i}")
    i=i+2 #number of stars increment by 2 for printing odd numbers of stars
    