# other methods in set

# 1) isdisjoint()
# checks if both sets have diff elements 
a={2,5,3,4,6,2} 
# b={2,5,3,4,6,2} will return false as 4 element matches set a
b={7,8,9} #returns true as no element matches the set a
print(a.isdisjoint(b))
print('-------------------------')

# 2)issuperset()
# checks if all the items of the original set is present in other set
a={'rasmalai','kulcha paratha','khakra'}
b={'aamras','rasmalai','puranpoli','rassa samosa','khakra','maggi'}
# will return false as all elements of original list a are not present in set b
print(a.issuperset(b)) 
print('-------------------------')

# 3)issubset()
# Checks if a set contains all the elements of another set.
a={23,56,45,78,98}
b={56,78}
# method checks if the set b elements present in set a(original set)
print(b.issubset(a))
print('-------------------------')

# 4)add()
# to add single item to a list
a={'A','F','R','S','U','Z'}
a.add('B')
print(a)
print('-------------------------')

# 5)update()
# updates the current set, by adding items from another set (or any other iterable).
x = {"facebook","amazon","flipkart"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
print('-------------------------')

# 6)remove and discard method
# remove an item in a set and if the item to remove does not exist, remove() will raise an error.
# discard an item in a set without raising an error
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") #if no value then it returns error
print(fruits)
fruits1 = {"apple", "banana", "cherry"}
fruits1.discard("banana")
print(fruits1)
print('-------------------------')

# 7)pop()
# to remove an item but this method will remove a random item so you cannot be sure what item gets removed.
# The return value of the pop() method is the removed item.
city = {"Amravati", "Pune", "Nagpur"}
x = city.pop()
print("poped item : ",x)
print(city)
print('-------------------------')

# 8)del()
# del keyword deletes the set entirely 
city = {"Amravati", "Pune", "Nagpur"}
del city
# print(city) #raises error as the set is deleted entirely along with variable
print('-------------------------')

# 9) clear()
car={'BMW','Rolls-Royce','Suzuki','Scorpio','Nano'}
print(car.clear()) # will return empty set as it clears all the elements in the set

