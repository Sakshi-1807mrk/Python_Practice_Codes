# methods in set

# 1)union and update method
# add two sets
a={'Madina','Jammu Kashmir','Banglore','Makka'}
b={'Paris','Switzerland','India'}
c=a.union(b) #returns new set
a.update(b) #adds item to existing string from another set
print("by union method:",c)
print("by update method:",a)
print("------------------------------------------------------------------")

# 2)symmetric_difference and symmetric_difference_update
# prints items that are not similar in both sets
a={2,5,3,4,6,2}
b={4,7,8,9,3,2}
c=a.symmetric_difference(b)#returns new set
a.symmetric_difference_update(b)
print("by symmetric_difference :",c) 
print("by symmetric_difference_update:",a)
print("------------------------------------------------------------------")

# 3)intersection and intersection_update
# similar items in both sets
a={5,10,15,20,25,30,35,40}
b={10,20,30,40,50,60}
c=a.intersection(b)#returns new set
a.intersection_update(b)
print("by intersection :",c) 
print("by intersection_update:",a)
print("------------------------------------------------------------------")

# 4)difference and difference_update
# items present only in original set 
a={'Switzerland','Jammu Kashmir','Banglore','Paris'}
b={'Paris','Switzerland','India'}
c=a.difference(b)#returns new set
a.difference_update(b)
print("by difference:",c) 
print("by difference_update:",a)


