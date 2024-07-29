# 1)program using function to convert celcius to fahrenheit

def temperature(celcius):
    fahrenheit=(celcius*9/5)+32
    print(f"Temperature in fahrenheit :{fahrenheit} ")
celcius=int(input("Temperature in Celcius :"))
temperature(celcius)
print("---------------------------------------")
# 2)program to convert inches into centimeters using functions

def centimeter(inches):
    cm=inches*2.54
    print(f"{inches} inches is {cm} centimeters")
inches=int(input("inches :"))
centimeter(inches)