import numpy as np
import os
import sys
import pyautogui as py
import cv2
import time
#from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)


x = 0
i = 0
while x < 10000000:
    if x % 2000000 == 0:
        print(i)
        i = i+1
    x = x+1
print("Go!")

while True:
      first = time.time()

#Image Grabbing
      image_np = py.grab(region = (650,220, 700, 300))
      image_mod = cv2.cvtColor(np.array(image_np),cv2.COLOR_BGR2GRAY)
      image_np = cv2.cvtColor(np.array(image_np),cv2.COLOR_BGR2RGB)
      edges = cv2.Canny(image_mod,100,200)
#Object detection
      matcher = cv2.matchTemplate(image_mod, template, cv2.TM_CCOEFF)
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matcher)
      top_left = min_loc
      bottom_right = (top_left[0] + w, top_left[1]+ h)
      cv2.rectangle(image_np,top_left, bottom_right, 255, 2)
#Decision making and key pressing
     #py.keyDown(' ')
     #py.keyUp(' ')

#Image Display
      cv2.imshow("Winning", cv2.resize(edges, (700,300)))
      #cv2.moveWindow("Winning", 2000, 0)

#Debug Functions
      print( "Loop Took: ", (time.time()-first))
      if cv2.waitKey(25) & 0xFF==ord('q'):
         cv2.destroyAllWindow()
         break
