# else with while loop 

i=0
while(i<=5):
    print("Smile")
    i+=1
else:
    print("This is else block")
print("-----------------------")

# else with while loop with interuption
i=0
while(i<=5):
    print(i)
    i+=1
    if(i==2):
        break
else:
    print("else block won't be executed")   