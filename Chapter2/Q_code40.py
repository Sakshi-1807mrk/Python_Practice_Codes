# program to greet all the person names stored in a list l1 which starts with s letter according to time
import time
current_hour=int(time.strftime("%H"))
l1=['Ria','Mayuri','Sakshi','Anu','Sanskruti']
for l in l1:
    if( not l.startswith("S")):#logical operator not
        continue
    if(current_hour<12):
       greeting="Good Morning !"
    if(current_hour<18):
        greeting="Good Afternoon !"
    if(current_hour<20):
        greeting="Good Evening !"
    else:
        greeting="Good Night !"
    print(f"Hello {l}, {greeting}")
       
