# import matplotlib.pyplot as plt
# import matplotlib.image as matimg # matimg=matplotlib image
from PIL import Image, ImageDraw, ImageFont
print("\n __!! MASTER OF TECHWORLD !! __ \n") 
play_game=input(" Do you want to play MAT ? ") 
play_game.lower() 
if (play_game=="yes") :
 print("\nWelcome to Master of TechWorld !!\n")
 response=input("Are you excited for this brain-tricking game ?\n")
 name=input("Please may we know your name :")
 if(response.lower()=="yes"):
  print("Rules for the MAT game :")
  print(" 1)You'll need to answer all the questions for winning the MAT trophy")
  print(" 2)For each questions, one score will be awarded for every correct option selected.")
  print(" 4)Please choose your options carefully to maximize your score!") 
  print(" 3)For score more than 10 you'll be awarded with a MAT certificate.\n")
  print("Get ready to have your technical skills challenged like never before!\n") 
  questions=[]
  opt=['C','C','B','A','D','C','D','A','D','B','B','C','D','A','A']
  questions.append(("1. What is the most popular programming language used for web development?",['A) Java','B) Python','C) JavaScript','D) C++']) ) 
  questions.append(("2. What is the name of the popular open-source operating system?",['A) Windows','B) macOS','C) Linux','D) Chrome OS']) ) 
  questions.append(("3. What is the name of the popular programming language developed by Brendan Eich?",['A) Java','B) JavaScript','C) Python','D) C++']) ) 
  questions.append(("4. What is the name of the popular web browser developed by Google?",['A) Chrome','B) Firefox','C) Safari','D) Edge']) ) 
  questions.append(("5. What is the latest version of the Python programming language?",['A) 3.9','B) 4.0','C) 3.11','D) 3.10']) ) 
  questions.append(("6. Which of the following data structures is used to store elements in a key-value pair?",['A) Array','B) Linked List','C) Hash Table','D) Stack']) ) 
  questions.append(("7. Which of the following is a popular framework for building web applications?",['A) React','B) Angular','C) Vue.js','D) All of the above']) ) 
  questions.append(("8. What is the purpose of the git version control system?",['A) To manage source code','B) To manage packages','C) To manage dependencies','D) To manage databases']) ) 
  questions.append(("9. Which of the following is a type of database management system?",['A) Relational','B) NoSQL','C) Graph','D) All of the above']) ) 
  questions.append(("10. What is the difference between a process and a thread?",['A) A process is a thread,a thread is a process','B) A process has its own memory,a thread shares memory','C) A process is used for I/O operations,a thread is used for CPU operations','D) A process is used for CPU operations,a thread is used for I/O operations']) ) 
  questions.append(("11. Which of the following is a popular algorithm for finding the shortest path in a graph?",['A) Binary Search','B) Floyd-Warshall algorithm','C) Kruskals algorithm','D) Bubble Sort']) ) 
  questions.append(("12. What is the purpose of the HTTP protocol?",['A) To manage email','B) To manage files','C) To manage web requests','D) To manage databases']) ) 
  questions.append(("13. Which of the following is a type of cloud computing service?",['A) IaaS','B) PaaS','C) SaaS','D) All of the above']) ) 
  questions.append(("14. Which company developed the React JavaScript library?",['A) Facebook','B) Google','C) Amazon','D) Microsoft']) ) 
  questions.append(("15. Which of the following is a type of network protocol?",['A) TCP/IP','B) HTTP','C) FTP','D) DNS']) ) 
  print("So this is the very first question on your screen. ") 
  i=0
  j=0
  score=0
  for i in range(len(questions) ) :
    print(f" {questions[i][0]}") 
    for options in questions[i][1]:
     print(f" {options}") 
    ans=input("Answer :")     
    if(ans.upper() ==opt[j]) :
     print("Your answer is Correct\n")
     score+=1 
    else:
     print(f"Your answer  is Incorrect\nThe correct option is {options}.\n") 
    j+=1
  print("Your final score is:", score)
  print("Your wrong choices are:",15-score)
  print("\n")
  if (score==15):
   # use the raw string (prefix the string with 'r') to avoid issues with backslashes
  #  img=matimg.imread(r'C:\Users\HP\Downloads\MAT img.jpeg')
  #  # to display the image
  #  plt.imshow(img)
  #  plt.axis('off') #  hide axis
  #  plt.show()
   img = Image.open(r'C:\Users\HP\Downloads\MAT img.jpeg')
   draw = ImageDraw.Draw(img)
   font = ImageFont.truetype('arial.ttf', 20)
   draw.text((10, 10), 'Hello, World!', font=font)
   img.show()
  # if(score==15):
  #  a='*'
  #  n=25
  #  while(n>=6):
  #   print(a*n)
else:
  quit() 
