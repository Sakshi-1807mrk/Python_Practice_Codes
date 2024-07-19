# practice exercise
# to display a user enetered name followed by Good Afternoon using input function
name=input('Enter your name:')
print("Good Afternoon,",name)

# write a program to fill in a letter template given below with name and date

a=name
date="20/07/2024"
#f is prefix indicating f-string that allows you to create strings that contain values from variables
Letter=f'''Dear {a},    
 Congratulations💐 ,You are selected !   
 {date}'''
print(Letter)

# program to detect double spaces
string="Success  demand    Sacrifice   "
double_space=string.count("  ")
print(f"there are {double_space} double spaces in the string ")

# program to replace double spaces in the above program with single spaces
string="Success  demand    Sacrifice  "
print(string.replace("  "," "))

# program to format a string using escape sequence character

Letter=f'Dear {a},\nCongratulations💐 ,You are selected !\n\t{date}'#\t adds space between words
print(Letter)
