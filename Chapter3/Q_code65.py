# binary search tree
def build_bst(my_list):
    if(len(my_list)==0):
        return "The list is empty"
    else:
        num=int(input("Enter the num to find :"))
        if(num in my_list):
         index=my_list.index(num)
         print(f"{num} is at index {index}")
        else:
          return "The number is not in the list" 
my_list=[1,2,4,5,6,7,8,9]
print(my_list)
build_bst(my_list)
