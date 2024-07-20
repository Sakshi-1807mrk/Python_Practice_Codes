# program to greet according to the current_time
import time
# the time module helps give the current working time in python
current_time = time.strftime( "%H:%M:%S")
# strftime is a function of module time that gives the current time and format the time into string
print(current_time)
# current_hour contains the string hour part of current_time converted in int type
current_hour=int(time.strftime("%H"))
if(current_hour<12):
  greeting="Good Morning !"
elif(current_hour<18):
  greeting="Good Afternoon !"
elif(current_hour<20):
  greeting="Good Evening !"
else:
  greeting="Good Night !"

print(greeting)