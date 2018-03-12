'''
Code written with inspiration and guidance from SENTDEXS Tutorial below
Code and videos
Youtube:
Github: https://github.com/Sentdex/pygta5
His code version link: https://github.com/Sentdex/pygta5/blob/master/1.%20collect_data.py#L20

My changes:
	-Repurposed lists for my keys
	-Added stop functionality and changed pause Functionality
	-Changed input detector to accept down arrow key
	 aka changed input of get_keys() to deal with hexadecimal and ASCII
	-changed Screen capture to use linux
	-changed get_keys to use linux
	-Reworked Pause functionality

Damon Hunka
'''


import numpy as np
import pyautogui as py
import cv2
import time
import os
from Presses import getch


'''
TO DO
1). File Save and Write functionality DONE
2). Pause Functionality DONE
3). Get indent Debugger for python
4). Profit ??? Mai Dai
'''

up = [1 , 0]
dw = [0 , 1]
no = [0 , 0]


startingvalue = 1
## While Loop for Initializing the correct trainingData Start
while(true):
	filename = 'trainingData-{}.npy'.format(startingvalue)
	if (os.path.isfile(filename)):
		print('trainingData-{} exists'.format(startingvalue))
		startingvalue = startingvalue + 1
	else:
		print('trainingData-{} does not exist ---> CREATING...'.format(startingvalue))
		print('...')
		print('...--STARTING TRAINING--...')
		break

## Function for comparing output
def Output(ch):
	output = no
	if ch == "20": #'20 is hexadecimal ASCII for ' '
		result = up
		print("up")				#
	elif ch == "1b":#1b is hexadecimal ASCII for '|'
		result = dw                	#            'V'
		print("down")
	return result

def main(filename, startingvalue):
	file_name = filename
	starting_value = startingvalue
	trainingData = []
	time1 = time.time()
	paused = False;
	#Main Loop
	while(True):
		#Pause Functionality
		if paused:
			key = getch()
			if key == "70":
				print("--Unpaused--")
				paused = False
				time.sleep(0.1)
		else:
			#Screen Capturing..
	        image_np = py.grab(region = (650,220, 700, 300))
	        image_np = cv2.cvtColor(np.array(image_np) , cv2.COLOR_BGR2GRAY)
	        image_np = cv2.Canny(image_np , 100,200)
	        image_np = cv2.resize (image_np, (480,206))

			#Key Press reading
			key = getch()
			KeyTrainer = Output(key)
			trainingData.append([image_np , KeyTrainer)

			#Pause reader
			if key == "70":
				paused = True
				print("--Pausing--")

			#Saving Function
			if len(trainingData)%100:
				print('Training Data: ', len(trainingData))
				#Saver
				if len(trainingData) == 500:
					print("...--SAVING--...")
					np.save(file_name,trainingData)
					trainingData= []
					startingvalue = startingvalue +1
					filename = 'trainingData-{}.npy'.format(startingvalue)

#Start Relief
x = 0
i = 0
while x < 10000000:
    if x % 2000000 == 0:
        print(i)
	    i = i+1
    x = x+1
print("Go!")
main(filename,startingvalue)
