"""
ListSpammer v1.1.1
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
f = open("spam.txt" , encoding='utf-8')
queueList = f.readlines()
queueList = [s.rstrip() for s in queueList] # stripping off \n
f.close()
print("Currently queued spam:")
print(queueList)
print('')

spamDelay = input("Delay (in seconds) between lines? If not, enter 0. : ")
times = input("Times to repeat spam? ")

input("Get ready to select your text box, then, press enter to start countdown...")

for s in range(secondsWait):
    print("Spamming in " + str(secondsWait) + " seconds...")
    time.sleep(1)
    secondsWait = secondsWait - 1
print("Spamming now!")

queueNumber = 0



for t in times:
    while True:
        try:
            currentLine = queueList[queueNumber]
            print("Spamming: " + currentLine)
            pyautogui.typewrite(currentLine)
            pyautogui.typewrite(['enter'])
            queueNumber = queueNumber + 1
            time.sleep(float(spamDelay))
        except IndexError:
            print('')
            print("Done!")
            break
