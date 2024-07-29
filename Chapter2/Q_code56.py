#1)print a tuple
tuple=(2,5,6,3,4,5)
print(tuple)
print('-------------------------------------')
# 2)concatenation of tuple 
tuple_num=(1,2,3,4,5)
tuple_num1=(6,7,8,9,10)
print(tuple_num+tuple_num1)
print('-------------------------------------')
#3)program to count the number of students with the “A” grade in the following tuple.
tuple=('A','D','B','A','C','B','D','B')
print(tuple.count('A'))
'''count method count the number of A grade in tuple'''
print('-------------------------------------')
#4) index of particular element
tuple_cars=('BMW','Rolls-Royce','Suzuki','Scorpio','Nano')
print(tuple_cars.index('Suzuki'))
'''element at particular index'''
print(tuple_cars[1])
print('-------------------------------------')
# 5)creating a tuple using user input
list=[]
tuple_items=int(input('Enter the number of elements in tuple :'))
for i in range(tuple_items):
    item=input(f"Enter the element {i}:" )
    list.append(item)
tuple_updated=tuple(list)
print(tuple_updated)





