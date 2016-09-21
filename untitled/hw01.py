#Write a program that reads grades on midterm(0-100), final(0-100), quizzes(0-120), and
#lab projects(0-130) and then prints the overall grade(0-100). The scores are weighted as
#follows:
#Midterm: 25%
#Final: 25%
#Quiz: 10%
#Projects: 40%



import time # for delay when program ends
import os   # on windows, need OS to clear prompt
while True:
    os.system('cls')        #using os to clear the promp upon reboot.
    print("Welcome to Mike's grade calculator! I bet I wont crash!")
    def midterm(mterm):
        try:
            term=int(mterm)     #Make sure input is a number.
            if not -1<term<101:    #Input grade within parameters
                print("Invalid entry, please retry.")   #Give output for invalid input, return no variable.
                return None
            return term     #return term if meets parameters
        except:
            print("Invalid entry, please retry.")   #Give output for no input
            return None                             #return no variable
    while True: #Promp & begins loop for multiple invalid entries
        mid=midterm(input("Enter your Midterm grade: "))    #allows user to input into function
        if mid == 0:        #Took me hours to get this simple fix. Allows user to input "0" without looping
            mid = "0"
        if mid: break   #once "mid" is defined, loop ends

    def finals(ale):
        try:
            fin=int(ale)
            if not -1<fin<101:
                print("Invalid entry, please retry.")
                return None
            return fin
        except:
            print("Invalid entry, please retry.")
            return None
    while True:
        fnl=finals(input("Enter your Finals grade: "))
        if fnl == 0:
            fnl = "0"
        if fnl: break

    def quizes(quis):
        try:
            qzs=int(quis)
            if not (-1<qzs<120):
                print("Invalid entry, please retry.")
                return None
            return qzs
        except:
            print("Invalid entry, please retry.")
            return None
    while True:
        quiz=quizes(input("Enter your Quiz grade: "))
        if quiz == 0:
            quiz = "0"
        if quiz: break

    def projects(ject):
        try:
            pro=int(ject)
            if not -1<pro<131:
                print("Invalid entry, please retry.")
                return None
            return pro
        except:
            print("Invalid entry, please retry.")
            return None
    while True:
        prj=projects(input("Enter your Project grade: "))
        if prj == 0:
            prj = "0"
        if prj: break
    #Function used for calculations
    def grade(mid,fnl,quiz,prj):
        #Changing previous variables from int to float for calculations, another part of fix for "0" as user input
        mid = float(mid)            #(helped me solve issue of 0 not being accepted as input)
        fnl = float(fnl)
        quiz = float(quiz)
        prj = float(prj)
        #Getting percantage for scores (0-100)
        mid = (mid/100)
        fnl = (fnl/100)
        quiz = (quiz/120)
        prj = (prj/130)
        #Weighting scores and assigning new variables.
        lb1 = (mid*0.25)
        lb2 = (fnl*0.25)
        lb3 = (quiz*0.1)
        lb4 = (prj*0.4)
        weight = [lb1,lb2,lb3,lb4]
        grade = sum(weight)*100 #getting final value
        return grade    #output is final value "grade"

    done=grade(mid,fnl,quiz,prj)    #Assigning variable to function to simplify call
    print("Your overall grade is: ",round(done),"or",round(done,2))

    reboot = input("Would you like to reboot? Y/N?: ")    #Ask for user input about rebooting
    reboot = reboot.lower()                             #Convert response to lower case
    if reboot != ("y"):                                 #input of anything but "y" will break loop, end program
        print("Thank you! I bet I didn't crash!"), time.sleep(2)
        break                                           #Messages for users, time.sleep so they have time to read.
    print("Rebooting..."), time.sleep(1)




















    # try:
    #     reboot = input("Would you like to reboot? y/n")
    #     if reboot == ("y"):
    #         return True
    #     if reboot == ("n"):
    #         return False
    #     raise ValueError
    # except ValueError:
    #     print("Would you like to reboot? y/n")
    #     return True
    # while True:
    #     print("Rebooting...")
    #     if not True: break






#
#     grade = (mid + fin + quiz + proj)* 100 # assign grade variable & change decimal to 0-100
#     print("Your overall grade is:", int(grade)) # Display overall grade
#
#     yn = input("Would you like to restart? Y/N ") #Ask user if they want to restart
#     if yn == "n":
#         print("Thanks for using my calculator!"), time.sleep(5), exit() # if "n" wait 5 seconds and exit
#     else:
#         print("rebooting...")
#
# while restart: #Should loop until closed or "restart"  is set to "False"
#     start()
#
