import numpy as np
import os
import sys
#import pyautogui as ImageGrab
import cv2
import time
import pyscreenshot as ImageGrab






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
      image =ImageGrab.grab(bbox =(1300,700, 1300, 250))
      #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image = np_array (image)




      cv2.imshow("Winning", cv2.resize(image, (1300,250)))
      #cv2.moveWindow("Winning", 2000, 0)

      print( "Loop Took: ", time.time()-first)
      if cv2.waitKey(25) & 0xFF==ord('q'):
         cv2.destroyAllWindow()
         break
