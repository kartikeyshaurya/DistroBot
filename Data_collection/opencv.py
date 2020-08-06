import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui 
import os 

dirName = "photos"
try:
    os.makedirs(dirName)    
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")  



'''
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("photos/in_emory_to_disk.png", image)
'''
intial = time.time()
for i in range(500):
    intial = time.time()
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("photos/%d.png"%i, image)
final = time.time()

total = final-intial
print("to print %d the code tool %d time")%500 %total