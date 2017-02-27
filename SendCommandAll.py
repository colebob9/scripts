"""
SendCommandAll v1
colebob9
Python 3

Sends a command to all configured Screen names.
"""

import subprocess
import shlex

# Config
screenName = ["test1" ,"test2"]
# End Config



print("Will send command to Screens: " + str(screenName))

serverCommand = input("Command? > ")

for s in screenName:
    print("Sending command: `" + serverCommand + "` to screen name \"" + s + "\"")
    subprocess.call(shlex.split("screen -S %s -p 0 -X stuff \"%s\n\"" % (s, serverCommand)))
