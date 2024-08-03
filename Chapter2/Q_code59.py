# set in python
# 1)create an empty set and print its type
a=set() # correct way of declaring empty set 
# a={} is wrong way as it will give dict type
print(type(a))
print("------------------------")
# 2)printing a set by taking user input in empty set
x=set()
set_ele=int(input("Enter the no. of elements want to insert in set :"))
for item in range(set_ele):
    item=input(f"Enter the element {item}:")
    x.add(item)
print(x)
print("------------------------")
# 3)accessing set elements
a={"sakshi","mayuri","sana"}
# it will show set elements in random order as they cannot be accessed by index
for i in a:
    print(i)
