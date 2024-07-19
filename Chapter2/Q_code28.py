# write a program whether a given name is present in list or not
list=["mango","grapes","pineapple","apple","watermelon","orange","jamun","strawberry","kiwi","guava"]
a=input("Enter the name of Fruit you want :")
# in membership operator returns true if user input fruit is in the list
if(a in list):
    print("Fruit is available in the market")
else:
    print("Fruit is not available in the market")