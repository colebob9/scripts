"""
ListSpammer v1
colebob9
Python 3

Spams text from a text file.

How to use:
Use `pip3 install pyautogui`.

Create a text file named `spam.txt` with the spam text inside. Each line will be separated with an Enter keypress.
"""

import pyautogui
import time

secondsWait = 5

print("Reading spam file...")
print('')
f = open("spam.txt")
global queueList
queueList = f.readlines()
queueList = [s.rstrip() for s in queueList] # stripping off \n
f.close()
print("Currently queued spam:")
print(queueList)
print('')

spamDelay = input("Delay (in seconds) between lines? If not, enter 0. : ")

input("Get ready to select your text box, then, press enter to start countdown...")

for s in range(secondsWait):
    print("Spamming in " + str(secondsWait) + " seconds...")
    time.sleep(1)
    secondsWait = secondsWait - 1

queueNumber = 0

while True:
    try:
        currentLine = queueList[queueNumber]
        pyautogui.typewrite(currentLine)
        pyautogui.typewrite(['enter'])
        queueNumber = queueNumber + 1
    except IndexError:
        print('')
        print("Done!")
        break