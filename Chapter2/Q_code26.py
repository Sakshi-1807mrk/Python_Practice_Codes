''' A program to find out to find whether a student is pass or fail if it requires 
total 40% and atleast 33% in each subject to pass.Assume 3 subjects and take marks 
from the user '''
# nested if-else
sub1=int(input("Enter Physics marks   :"))
sub2=int(input("Enter Chemistry marks :"))
sub3=int(input("Enter Maths marks     :"))
total=((sub1+sub2+sub3)/300)*100
if(sub1>=33 and sub2>33 and sub3>33):
    print("Student is passed in all three subjects")
    if(total>=40):
     print("Student is passed")
else:
    print("Student is failed")