# break statement

i=0
while(i<=10):
    print(i)
    if(i==8):
        break # break ends the loop as the iteration matches if condition
    i+=1
print("-------------------")
# program to print table of 5 which includes break keyword
x=1
while(x<=14):
    print(f"5 x {x} = {5*x}")
    if(x==10):
        break # break ends the loop as the iteration matches if condition
    x+=1