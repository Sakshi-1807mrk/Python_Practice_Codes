# methods in string
# 1.upper()
a='Python is Amazing'
print(a.upper()) #converts string to upper case
print('---------------------------------------------------------')

# 2.lower()
a='Python is Amazing'
print(a.lower()) #converts string to lower case
print('---------------------------------------------------------')
# 3.strip()
a='Python is Amazing       '
print(a.strip()) #removes whitespaces from string
print('---------------------------------------------------------')

# 4.rstrip()
a='Python is Amazing !!!!'
print(a.rstrip('!')) #removes trailling characters from string
print('---------------------------------------------------------')

# 5.replace()
a='Python is Amazing'
print(a.replace('Python','Java')) #replace a string with another string
print('---------------------------------------------------------')

# 6.split()
a='Python is Amazing'
print(a.split(' ')) #splits the string as list items
print('----------------------------------------------------------')
# 7.capitalize()
a='python is amazing'
print(a.capitalize()) #converts first character if string to uppercase and the rest to lowercase
print('---------------------------------------------------------')

# 8.center()
a='Python is Amazing'
print(a.center(50)) #aligns the string to center
print('---------------------------------------------------------')

# 9.count()
a='python is amazing'
print(a.count('n')) #returns the no. of times the given value is occured
print('---------------------------------------------------------')

# 10.endswith()
a='python is amazing !'
print(a.endswith('!')) #checks if the string ends with given value
print('---------------------------------------------------------')

# 11.find()
a='python is amazing !'
print(a.find('is')) #search for the 1st occurance of given value and returns its index
print(a.find('ish'))#returns -1 as ish is not present in string
print('---------------------------------------------------------')

# 12.index()
a='python is amazing !'
print(a.find('is')) #search for the 1st occurance of given value and returns its index
print(a.find('ish'))#returns valueerror as ish is not present in string
print('---------------------------------------------------------')

# 13.isalnum()
a='python is amazing no 1'
print(a.isalnum()) #returns true only if contains alphabets and numbers
print('---------------------------------------------------------')

# 14.isalpha()
a='python is amazing'
print(a.isalpha()) #returns true only if contains alphabets
print('---------------------------------------------------------')

# 15.islower()
a='python is amazing'
print(a.islower()) #returns true if string is in lower case
print('---------------------------------------------------------')

# 16.isprintable()
a='python is amazing \n' #\n therefore not printable
b='python is amazing '
print(a.isprintable()) #returns false if values in string are nonprintable 
print(b.isprintable()) #returns true if values in string are printable 
print('---------------------------------------------------------')

# 17.isspace()
a='         ' #using spacebar
b='         ' #using tab
print(a.isspace()) #returns true if string contains whitespace
print(b.isspace())
print('---------------------------------------------------------')

# 18.istitle()
a='Pyhton Java Javascript' 
print(a.istitle()) #returns true only if first letter of each word capital
print('---------------------------------------------------------')

# 19.isupper()
a='PYTHON PROGRAMMING' 
print(a.isupper()) #returns true if all characters are in uppercase
print('---------------------------------------------------------')

# 20.startswith()
a='Coding is cool' 
print(a.startswith('Coding')) #returns true if string starts with given value
print('---------------------------------------------------------')

# 21.swapcase()
a='Coding IS Cool' 
print(a.swapcase()) #swaps the cases of string
print('---------------------------------------------------------')

# 22.title()
a='nothing is immpossible' 
print(a.title()) #it capitalizes each letter of word in string
print('---------------------------------------------------------')





