# dictionary in python

# 1)program to create the dictionary for english words and their hindi translations
#   allowing the user to look up for the word
english_dict = {
    "hello":"नमस्ते",
    "thank you":"धन्यवाद",
    "please":"कृपया",
    "yes":"हाँ",
    "no":"नहीं",
    "i'm fine":"मैं ठीक हूँ",
    "how are you?":"आप कैसे हैं?",
    "excuse me":"माफ़ कीजिये",
    "sorry":"मुझे खेद है"
}
print("English Dictionary :")
print(english_dict)
def look_word():
    word=input("Enter the word :")
    word=word.lower()
    if word in english_dict:
        print(f"Hindi meaning for the word '{word}' is {english_dict[word]}")
    else:
         print("Sorry! word not found in the dictionary.")
look_word()
print("-------------------------------------------------")
# 2)an empty dictonary in which 4 friends gives values as their favourite lang and keys are their names
dict={}
user_input=int(input('Enter the number of entries in dictionary :'))
for items in range(user_input):
  key = input("Enter key: ") #user input key
  value = input("Enter value: ") #user input value
  dict[key] = value # assign key-value pair to dictionary
print("Dictionary :",dict)
print("-------------------------------------------------")
# 3) merging two dictionaries
dict1={"pink":"pinklily","yellow":"sunflower","blue":"blue daisy"}
dict2={"red":"rose","white":"jasmine"}
dict1.update(dict2)
print(dict1)

    
