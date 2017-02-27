"""
ListSpammer v1.1
colebob9
Python 3

Spams text from a text file.

How to use:
Use `pip3 install pyautogui`.

Create a text file named `spam.txt` with the spam text inside. Each line will be separated with an Enter keypress.
"""

import pyautogui
import time

# Config
secondsWait = 5
# End Config

# Read spam.txt
print("Reading spam file...")
print('')
f = open("spam.txt")
spamList = f.readlines()
spamList = [s.rstrip() for s in spamList] # stripping off \n
f.close()
print("Currently queued spam:")
print(spamList)
print('')

spamDelay = input("Delay (in seconds) between lines? If not, enter 0. : ")

input("Get ready to select your text box, then, press enter to start countdown...")

for s in range(secondsWait):
    print("Spamming in " + str(secondsWait) + " seconds...")
    time.sleep(1)
    secondsWait = secondsWait - 1

for l in spamList:
    pyautogui.typewrite(l)
    print(l)
    pyautogui.typewrite(['enter'])
