# variable length arguments in function
 
# program for Arbitrary Arguments
# * is added before parameter name so that function access the arguments processing them in the form of tuple
def helping_verb(*verb):
    print(f"Some of the helping verbs are : {verb[0]}, {verb[1]}, {verb[2]}")
helping_verb('is','are','was') # acts as tuple

# program for Keyword Arbitrary Arguments
# ** is added before parameter name so that function access the arguments processing them in the form of dictionary
def names(**names):
    print(f"Merry Christmas ! {names['a']}, {names['b']}, {names['c']}")
names(a='Elsee',b='Rosemary',c='Christina') # acts as dictionary



