# for else to search for an element
numbers = [10, 20, 30, 40, 50]
target = 30

for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found in the list.")
print("---------------------------------------")
# for else to check for prime number
num=int(input("Enter the number :"))
for i in range(2,num):
    if(num%i==0):
        print(f"{num} is not prime number ")
        break
else:
    print(f"{num} is prime number")

# first composite number in list
list=[3,5,7,11,4,8]
for i in list:
    for j in range(2,i):
        if(i%j==0):
            print(f"{i} is first composite number in list")
            number=True
            break
    if number :
        break
else:
    print("There is no composite number in list ")