# string format method
string="hey {name} , how are you doing these days. You live in {place} right "
print(string.format(place="Amravati",name="Sakshi"))
txt = "For only {price:.2f} dollars!"
# .2 specifies the number of decimal places to 2.
# f converts the number to float
print(txt.format(price = 49))

# formatting using f-string 
name="Sakshi"
print(f"hello {name}, how was your day")