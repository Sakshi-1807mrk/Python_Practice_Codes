# Else with for Loop

for i in range(7):
   print(i)
# else block is completed after the all iterations in loop are completed
else:
  print("This is the else block")
print("---------------------------")

# else in loop for empty list
for i in []:
   print(i)
else:
   print("Else block is executed as there are no items for iteration in loop")
   print("---------------------------")

# else in loop using break statement
for i in range (6):
   print(i)
   if (i==4):
      break
# here as the loop is interuppted using break statement the else block wont be executed
# as the code exits the loop after the execution of else block
else:
   print("Else block won't be executed")
