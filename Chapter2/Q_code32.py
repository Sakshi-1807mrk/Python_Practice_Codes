# match case statement
# program to find the day of the week
day=int(input("Enter the nth day of week :"))
match(day):
    case 1 :
        print("It's Sunday today !")
    case 2 :
        print("It's Monday today !")
    case 3 :
        print("It's Tuesday today !")
    case 4 :
        print("It's Wednesday today !")
    case 5 :
        print("It's Thursday today !")
    case 6 :
        print("It's Friday today !")
    case 7 :
        print("It's Saturday today !")
    case _:
        print("There are only 7 days in week you have entered invalid day")
        