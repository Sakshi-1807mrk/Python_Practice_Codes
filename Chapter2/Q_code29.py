# write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100:Ex,80-90:A,70-80:B,60-70:C,50-60:D,<50:E
marks=int(input("Enter the total marks obtained out of 500 :"))
percentage=((marks)/500)*100
if(90<=percentage<=100):
    print("The grade is EX")
elif(80<=percentage<=90):
   print("The grade is A") 
elif(70<=percentage<=80):
   print("The grade is B") 
elif(60<=percentage<=70):
   print("The grade is C") 
elif(50<=percentage<=60):
   print("The grade is D") 
else:
   print("The grade is E")