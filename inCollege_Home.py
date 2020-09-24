#Front page
#Displays the selected options (and sub-options, if applies)
#calls the relevant functions correlating to user input
import inCollege_Accnt as accnt
import inCollege_Database as database
import inCollege_CurrentUser as user

def skillScreen():
    print("")
    print("1. Python")
    print("2. Java")
    print("3. C++")
    print("4. Teams")
    print("5. Git")
    sel = int(input("Please make a selection. Input any number not listed above to return to main menu: "))
    if sel in range(1,6):
        print("Under construction.")
        return True
    return False
    

# def selectionScreen(val):
#     if val in range(1,6):
#         print("Under construction.")
#         return True
#     return False

def mainMenuIntroMessage():
    print("When I was in college, I didn't know what to do with myself.")
    print("I was well on my way to graduation, but I had no experience, no internships lined up, nothing.")
    print("Then a friend pointed me to inCollege and it changed my future forever.")
    print("InCollege is a wonderful tool to connect college hopefuls to one another and to future employers.")
    print("It's easy to use and it gave me results in no time at all.")
    print("I went from having no prospects to an internship at a major company in a matter of weeks!")
    print("It's not an exaggeration to say that I wouldn't have been as successful as I am without inCollege.")
    print("So I can't recommend it enough. Give it a chance and it will change your life for the better!")
    print("--Dick Tracey, Computer Science Graduate from USF, Chief Software Engineer at Microsoft.")
    print("")

    print("Would you like to know more?")
    sel = -1
    done = False
    while (sel != 0):
        sel = int(input("Input 1 to view the video. Input 0 to skip: "))
        if (sel == 1):
            print("Video is now playing.")
            break
        elif (sel == 0):
            print("Video was skipped")
            break
        else:
            print("Invalid input. Input 1 to view the video. Input 0 to skip.")
    print("")

def loginPrompt(foundUser):
    sel = -1
    if (foundUser == True):
        print("Would you like to login or sign up for an account?")
        while (sel != 0):
            sel = int(input("Input 1 to log in. Input 2 to sign up. Input 0 to continue without logging in or signing up: "))
            if (sel == 0):
                continue
            elif (sel == 1):
                theUser = accnt.login()
                return theUser
                break
            elif (sel == 2):
                accnt.create_account()
                print("Please log in from the home page!")
                break
            else:
                print("Invalid selection. Input 1 to log in. Input 2 to sign up. Input 0 to continue without logging in or signing up: ")
    return False
    
def main ():
    mainMenuIntroMessage()
    DB = database.Database()
    loginStatus = False
    sel = -1
    print("Welcome to InCollege!")
    while (sel != 0):
        #This menu is displayed to non-logged in user
        if (loginStatus == False):
            print("")
            print("1. Login")
            print("2. Create New Account")
            print("")
            print("3. Job/Internship Search")
            print("4. Find Someone You Know")
            print("5. Learn a New Skill")
            print("")
            sel = int(input("Please make a selection, input 0 to Quit: "))
            print("")
            if (sel == 0):
                print("Goodbye!")
            elif (sel == 1):
                # if log in is successful, the user object is returned. Otherwise, false is returned.
                theUser = accnt.login(DB)
                if theUser is False:
                    loginStatus = False
                else:
                    loginStatus = True
            elif (sel == 2):
                accnt.create_account(DB)
            elif (sel == 3):
                print("Under construction.")
            elif (sel == 4):
                
                foundUser = DB.search_users()
                theUser = loginPrompt(foundUser)
                if theUser is False:
                    loginStatus = False
                else:
                    loginStatus = True
            elif (sel == 5):
                skillScreen()
            elif (sel == -100):
                accnt.clear_accounts()
            else:
                print("Invalid Selection!")
        #This menue is displayed for logged in user
        else:
            print("")
            print("1. Post a Job")
            print("")
            print("2. Job/Internship Search")
            print("3. Find Someone You Know")
            print("4. Learn a New Skill")
            print("")
            sel = int(input("Please make a selection, input 0 to Quit: "))
            print("")
            if (sel == 0):
                print("Goodbye!")
            elif (sel == 1):
                accnt.post_job(theUser.name, DB)
            elif (sel == 2):
                print("Under construction.")                
            elif (sel == 3):
                db = database.Database()
                db.search_users()
            elif (sel == 4):
                skillScreen()
            elif (sel == 6):
                accnt.clear_accounts()
            else:
                print("Invalid Selection!")


    #Ignore everything between '====='
    #=========================================================
    db = database.Database()
    print("Students in database: ", db.data["Students"])
    print("Jobs in database: ", db.data["Jobs"])
    #=========================================================

if __name__=='__main__':
    main()
