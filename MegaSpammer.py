"""
MegaSpammer v1.1
Python 3
colebob9

Spams any text box with as much text as you want.

Use `pip3 install pyautogui`.
"""

import pyautogui
import time

secondsWait = 5

# ask for input
spamContent = input("Content of spam?: ")
spamTimes = input("How many times?: ")
spamDelay = input("Delay (in seconds) between messages? If not, enter 0. : ")

input("Get ready to select your text box, then, press enter to start countdown...")

for s in range(secondsWait):
    print("Spamming in " + str(secondsWait) + " seconds...")
    time.sleep(1)
    secondsWait = secondsWait - 1

for t in range(int(spamTimes)):
    pyautogui.typewrite(spamContent)
    pyautogui.typewrite(['enter'])
    time.sleep(float(spamDelay))
