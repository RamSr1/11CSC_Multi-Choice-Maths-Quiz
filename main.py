
while True:
     print("╔════════════════════════════════════════╗")
     print("")
     n = input("  Please enter your name ➣ ")
     if n.isalpha():
         print("    ----------------------")
         print("    Hello! " +      n)
         print("    ----------------------")
         print("")
         break
     else:
         print("  Please enter you name with letters only, and don't leave empty")
         

inst=input("  Press any key to proceed  :")
print("")
print("╚════════════════════════════════════════╝")
if inst=="y":
    print("you can choose any number of rounds")
    print("choosing a small number is easy")
else:
    print("")
    print("⌠ Welcome to my Math quiz ⌡")
    print("")
#The Instructions/Knowledge for the user to keep in mind;
print("\033[4mHow This Quiz Will Work:\033[0m")
print("")
print("╔═══════════════════════════════════════════════════════════════════════════════╗")
print("")
print("1) \033[4mThis Quiz Will Have A Total Of 12 Question For You To Answer.\033[0m")
print("")
print("2) \033[4mYou Will Have 1 Chance To Answer Each Question Correctly.\033[0m")
print("")
print("3) \033[4mEvery Question Will Include A Range Of Different Math Skills.\033[0m")
print("")
print("4) \033[4mEach Question Has It's Own Difficulty And Are Randomised.\033[0m")
print("")
print("5) \033[4mQuestions Will Consist Of Achieved, Merit Or Excellence Difficulty.\033[0m")
print("")
print("6) \033[4mAnswer Carefully As Every Question Counts Towards Your Final Score.\033[0m")
print("")
print("7) \033[4mThis Quiz Is To Prepare and Test Your NCEA Level 1 Maths Skills.\033[0m")
print("")
print("╚════════════════════════════════════════════════════════════════════════════════╝")
print("") 
print("")
print("╔════════════════════════════════════════════════════════════════════════════════╗")
print("")
print("\033[4m Here is a 3 question warmup, this won't affect your grade it is just a starter.\033[0m")

score = 0

# QUESTION 1
answer1 = input("What is 2 * 20 ? \n a. 35 \n b. 40 \n c. 28 \nAnswer: ")
if answer1 == "b" or answer1 == "40":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The right answer is 40")
    print("Score: ", score)
    print("\n")
# QUESTION 2
answer2 = input("What is 5 * 50 ? \n a. 350 \n b. 400 \n c. 250 \nAnswer: ")
if answer2 == "c" or answer2 == "250":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The right answer is 250")
    print("Score:", score)
    print("\n")
# QUESTION 3
answer3 = input(
    "What is 4 * 245.6 ? \n a. 345.8 \n b. 982.4 \n c. 456.6 \nAnswer: ")
if answer3 == "b" or answer3 == "982.4":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The right answer is 982.4")
    print("Score:", score)
    print("\n")
  #FINAL MESSAGE
if score <= 1:
    print("You total score:", score, "- You did Okay!")
elif score == 2:
    print("You total score:", score, "- You did Good!")
elif score == 3:
    print("You total score:", score, "- You did Amazing!")
print("╚════════════════════════════════════════════════════════════════════════════════╝")
print("")
print("")
print("╔════════════════════════════════════════════════════════════════════════════════╗")
print("--) \033[4m-Now that is over we can move on to the actual quiz\033[0m")
#How many points each question is worth;
print("Scoring System:")

print("Achieved Questions:+ 1 POINT")
print("Merit Questions:+ 2 POINTS")
print("Excellence Questions:+ 3 POINTS")
print("")

score=0
questions={'\033[4mQuestion 1\033[0m.\nSam is starting his own taxi company.He will charge $8 per hour,along with a fixed charge of $15,Find the Equation of Sams Pricing plan, when x is = hours\na:15x+8\nb:8x+15x\nc:8x+15 \n' : 'c' , 
'\033[4mQuestion 2\033[0m\nA building inspector wants to check if the pillar of the building is perpendicular to the ground. He measures the distance between 3 points, Each distance measures 3.11m, 4.19m and 5.23m. Is the pillar of the building of the building perpendicular to the ground.\na:Yes\nb:No\nc:Impossible to tell \n' : 'a' ,
'\033[4mQuestion 3\033[0m\nVishwnath takes 40 minutes to jog the 5 km from his home to school. What  is the average speed when he is jogging from his home to school?\na:1.15km/min\nb:0.125km/ min\nc:0.5km/min\n' : 'b' ,
'\033[4mQuestion 4\033[0m\nWhat is the value of 2x^4 − 3x + 5 when x = − 2?\na:44\nb:22\nc:43 \n' : 'c'}

for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        score += 1 
        print("")
        print("Good Job, That's Correct!")
        print("╚════════════════════════════════════════════════════════════════════════════════╝")
        print("")
        print("╔════════════════════════════════════════════════════════════════════════════════╗")
        print("")
        print("")
    else:
        print("")
        print("Incorrect")
      
        print("╚════════════════════════════════════════════════════════════════════════════════╝")
        print("")
        print("╔════════════════════════════════════════════════════════════════════════════════╗")



questions={'\033[4mQuestion 5\033[0m.\nFollwing on from question 2\nFrom 8m away from the bottom of the left side of the building he looks at the top of the bridge. The angle of elevation is 28 degrees. He is 1.83m  tall. Find the height of the building.\na:6.08m(2.d.p)\nb:6.56m(2.d.p)\nc:8.40m(2.d.p) \n' : 'a' ,
'\033[4mQuestion 6\033[0m\nFind the co-ordinates of which the follwing two lines intersect at.4x+10, 2x+18\na:(2,18)\nb:(-4,26)\nc:(4,26) \n' : 'c'
, '\033[4mQuestion \033[0m7\nGiven the equation -x/2(x-r)+2 find the equation of r given the point(8,2)\na:6\nb:8\nc:10\n' :  'b' 
,  '\033[4mQuestion 8\033[0m\n75% of homes on the national power supply in New Zealand are in the North Island. The rest are in the South Island. 70% of homes in the North Islandand 80% of homes in the South Island use electricity for their heating.   Calculate the probability that a home selected randomly across New Zealandis on the national power supply in the North Island AND uses electricity  for heating.\na: 0.5(1/2)\nb: 0.525(21/40)\nc: 0.593(16/27) \n' : 'b'}

for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        score += 2 
        print("Good Job, That's Correct!")
         
  
    else:
        print("Incorrect!")
      

questions={'\033[4mQuestion 9\033[0m\nRuru and Tane are standing on opposites sides of the net Tane sends the ball over the net towards Ruru. The equation of the path travelled by the volleyball is H=-0.25(x-2.1)^2+3.9.Find when the ball will hit the ground.\na:6m away from the net\nb:6.05m away from the net\nc12.24m  away from the net \n': 'b'
,'\033[4mQuestion 10\033[0m\nFollowing on from Question 8\nThere are 1 500 000 homes across New Zealand (both in the North Island and the South Island). Calculate how many of the homes on the national power supply in the South Island do not use electricity for heating. \na:75,000\nb:125,000\nc:265,000 \n' : 'a'
 
,'\033[4mQuestion 11\033[0m\n3/x+2+5/x-4=2\na:7,-1\nb:3,6\nc:7\n': 'a'
, '\033[4mQuestion 12\033[0m\n36x6^2x+6=6^x^2\na:x=4\nb:x=3,1\nc:x=4,-2\n':  'c'}

for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        score += 3
        print("Good Job, That's Correct!")
      
    else:
        print("Incorrect!")
print("")
print("")
print('Well done, you finished the quiz')
print("")
print('Congratulations your final score was {}/24'.format(score))
print("")
if 7>score:
  print("Your Final Grade Is \033[4mNot Achieved\033[0m Better Luck Next Time")
elif 14>score:
  print("Your Final Grade Was \033[4mAchieved\033[0m, Nice Work")
elif 19>score:
  print("Your Final Grade Is \033[4mMerit\033[0m, Fantastic!!")
else:
  print("Your Final Grade Was \033[4mExcellence\033[0m,That's Phenomenal,!!")
print("")
print("\033[4mCut Scores\033[0m")
print("")
print("\033[4mNot Achieved\033[0m =0-6\n\033[4mAchieved\033[0m =7-13\n\033[4mMerit\033[0m =14-18\n\033[4mExcellence\033[0m =19-24")
print("")
print('\033[4mThe answers to the questions are located below\033[0m ')
print("")

print("\033[4mAnswers\033[0m ")
print('Question 1:c\nQuestion 2:a\nQuestion 3:b\nQuestion 4:c\nQuestion 5:a\nQuestion 6:c\nQuestion 7:b\nQuestion 8:b\nQuestion 9:b\nQuestion 10:a\nQuestion 11:a\nQuestion 12:c')
print("")
print("\033[4mQuestions 1-4\033[0m= NCEA level 1 Achieved Questions\n\033[4mQuestions:5-8\033[0m= NCEA Level 1 Merit questions\n\033[4mQuestions:9-12\033[0m= NCEA level 1 Excellence Questions")
print("")
from colors import *

def clear():
  print("\033c",end="")

start_screen = f'''{Blue}
▒█▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ 　 ▀▀█▀▀ █░░█ █▀▀█ █▀▀ 
▒█▄▄█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█ 　 ░▒█░░ █▄▄█ █░░█ █▀▀ 
▒█░░░ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀ 　 ░▒█░░ ▄▄▄█ █▀▀▀ ▀▀▀{reset}'''

level_screen = f'''{bright_magenta}               ▒█░░░ █▀▀ ▀█░█▀ █▀▀ █░░ █▀▀ ▄ 
               ▒█░░░ █▀▀ ░█▄█░ █▀▀ █░░ ▀▀█ ░ 
               ▒█▄▄█ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀{bright_green}

        Beginner:         {Blue}Intermediate:         {bright_blue}Settings{reset}