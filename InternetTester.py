"""
InternetTester v2
Python 3
colebob9

Infinitely tests for pings during an internet outage until internet is back.

"""

# config
hostname = "google.com"   # site to ping
waitTime = 15     # time to wait between each ping command
# end config


import time
import os
import platform

makeSure = 0
platformName = platform.system()


if platformName == 'Windows':
        response = os.system("ping " + hostname)
else:
        response = os.system("ping -c 2 " + hostname)
        

while True:
        
	dateTime = time.strftime("%I:%M:%S %p")
	if response == 0:
		for t in range(5):
			print('')
			print("****" + "As of " + dateTime + ", " + hostname + " is up!" + "****")
		makeSure = makeSure + 1
	else:
		print("As of " +  dateTime + ", " + hostname + " is down.")
		makeSure = 0

	if makeSure == 3:
		break

	time.sleep(waitTime)
