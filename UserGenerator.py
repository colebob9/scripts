"""
UserGenerator v1
colebob9
Python3

For quickly generating username/passwords for websites. Mostly for throwaway accounts.
"""

import pyautogui
import time
import random
import string
import os


# Config

usernamePrefix = "GAHPLZTOHALP_"
passwordLength = 15        # Number of characters to make the password


# End config

global usernameList
global passwordList

# Have we run this code before? If not, create an empty list
if not os.path.isfile("usernameList.txt"):
    usernameList = []
else:
    # Read the file into a list and remove any empty values
    # If we have run the code before, load the list of posts we have replied to
    with open("usernameList.txt", "r") as f:
        usernameList = f.read()
        usernameList = usernameList.split("\n")
        usernameList = list(filter(None, usernameList))
        
if not os.path.isfile("passwordList.txt"):
    passwordList = []
    # Read the file into a list and remove any empty values
else:
    with open("passwordList.txt", "r") as f:
        passwordList = f.read()
        passwordList = passwordList.split("\n")
        passwordList = list(filter(None, passwordList))


while True:
    input("Press Enter to generate and type a username/password")
    print('')
    # Username Generation
    
    randomNumber = str(random.randint(1, 99999))
    username = usernamePrefix + randomNumber
    
    # Password Generation
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(passwordLength))

    
    if username not in usernameList:
        usernameList.append(username)
        print("This is your username: " + username)
        print("Your Password: " + password)
        passwordList.append(password)
        # Waiting to get ready.
        secondsWait = 5     # Number of seconds to wait before typing
        for s in range(secondsWait):
            print("Typing in " + str(secondsWait) + " seconds...")
            time.sleep(1)
            secondsWait = secondsWait - 1
        print("Typing now!")
        
        pyautogui.typewrite(username)
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(password)
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(password)
        
        # Write our updated list back to the file
        with open("usernameList.txt", "w") as f:
            for username in usernameList:
                f.write(username + "\n")
        with open("passwordList.txt", "w") as f:
            for password in passwordList:
                f.write(password + "\n")
    else:
        print("Found a duplicate! Try again.")