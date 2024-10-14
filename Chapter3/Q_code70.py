# sorting prime and composite numbers from list
list=[34,67,5,23,32,12]
list_1=[] # compositr number
list_2=[] # prime number
for i in list:
    for j in range(2,i):
        if(i%j==0):
            list_1.append(i)
            break
    else:
      list_2.append(i)
print("Composite Number :",list_1)
print("Prime Number     :",list_2)