# program to ask the user to enter the elements & store them in a list.

n=int(input("Enter the number :"))
list=[]
for i in range(n):
    list.append(input("Enter the element :"))
print(list)
print('-----------------------------------------')
# programs to accept marks of 6 students and display them in a sorted manner
student_marks=[]
for i in range(6):
    marks=int(input(f"Enter the marks of student {i} :"))
    student_marks.append(marks)
student_marks.sort()
print(student_marks)

