"""
InternetTester v1
Python 3
colebob9

Infinitely tests for pings during an internet outage until internet is back.

"""

import time
import os

makeSure = 0

while True:
	hostname = "google.com"
	response = os.system("ping -c 2 " + hostname)
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

	time.sleep(20)
