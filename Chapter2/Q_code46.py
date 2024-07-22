# program to print the following star pattern 
#  * * *
#  *   *
#  * * *
n=3 #number of rows(n)
# loop from 1 to n 
for i in range(1,n+1):
    #if condition helps print three stars for odd rows
    if (n%i==0): 
     print(f"{'* '*n}") 
    #else condition helps print the 2nd row pattern shown above for even rows 
    else:          
      print("*   *") 