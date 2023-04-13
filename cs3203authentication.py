import hashlib

def noSpaces(userOrPass):
    spaces = 1
    while(spaces > 0):
        spaces = 0
        for element in userOrPass:
            if(element == " "):
                spaces = spaces + 1

        if(spaces > 0):
            userOrPass = input("Please do not include spaces: ")

    return userOrPass

def listOfUsernames():
    file = open("logininfo.txt", "r")
    testing = file.readline()
    user = ''
    listOfUsernames = []

    #put list of all usernames in listOfUsernames
    while(testing != ''):
        for ch in testing:
            if(ch != " "):
                user = user + ch
            else:
                listOfUsernames.append(user)
                break

        user = ''
        testing = file.readline()
    file.close()
    return listOfUsernames

def userAlreadyTaken(user, Users):
    #Checks if the username is already taken
    enterya = True
    if(user == ''):
            while(enterya):
                user = input("Please enter something: ")
                user = noSpaces(user)
                if(user != ''):
                    enterya = False

    taken = False
    while(taken != True):
        for name in Users:
            if(name == user):
                taken = True

        if(taken):
            user = input("Username already taken. Please try again: ")
            user = noSpaces(user)
            enterya = True
            if(user == ''):
                while(enterya):
                    user = input("Please enter something: ")
                    user = noSpaces(user)
                    if(user != ''):
                        enterya = False
            taken = False
        else:
            break
    return user

################Beginning of Main#####################
newaccount = input("Are you a new user? (Y/N): ")

answered = False
while(answered != True):
    ###################### Signing up ###########################
    if(newaccount.lower() == "y"):
        answered = True
        newuser = input("Create a new account by entering a username (Do not include spaces): ")
        newuser = noSpaces(newuser)
        listOfUsers = listOfUsernames()
        newuser = userAlreadyTaken(newuser, listOfUsers)

        file = open("logininfo.txt", "a")
        file.write(newuser + " ")
            
        newpass = input("Please enter a password for this account (Do not include spaces): ")
        newpass = noSpaces(newpass)
        enterya = True
        if(newpass == ''):
            while(enterya):
                newpass = input("Please enter something: ")
                newpass = noSpaces(newpass)
                if(newpass != ''):
                    enterya = False
        hashresult = hashlib.md5(newpass.encode())
        file.write(hashresult.hexdigest() + "\n")
        file.close()
        ############################# Logging in ########################
    elif(newaccount.lower() == "n"):
        answered = True
        user = input("Please enter your username: ")
        listOfUsers = listOfUsernames()

        #Checks if input has an account
        until = True
        while(until):
            for co in listOfUsers:
                if(user==co):
                    until = False
            if(until):
                user = input("User does not exist. Try again: ")

        #Obtains hash related to the user
        file = open("logininfo.txt", "r")
        line = file.readline()
        hash = ''
        userline = ''
        start = False
        while(line != ''):
            for ch in line:
                if(start):
                    hash = hash + ch
                
                if(ch == " "):
                    if(userline == user):
                        start = True
                else:
                    userline = userline + ch
            line = file.readline()
            start = False
            userline = ''
        file.close()
        hash = hash.translate( { ord("\n"): None } )
        #print(hash)

        password = input("Please enter your password: ")

        #Checking if input password hash equals the hash stored in the file
        wrong = True
        while(wrong):
            passresult = hashlib.md5(password.encode())
            if(passresult.hexdigest()==hash):
                print("Congrats! You are now signed in.")
                wrong = False
            else:
                password = input("Error signing in. Please re-enter password: ")
    else:
        newaccount = input("Invalid answer. Try again: ")