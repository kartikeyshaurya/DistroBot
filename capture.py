import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui 
import pandas as pd 
import os 
import pygame 
from pygame.locals import *

count = 0


#--- Experimental code just too create pygame env ----#
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(0)




#--- creating a folder for the photos ---#
dirName = "photos"
try:
    os.makedirs(dirName)    
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

#--- code ended ---#

#--- putting in the pandas dataframe ---#
items = {'Images' : pd.Series(data = []),
         'left_side': pd.Series(data = []),
         'right_side': pd.Series(data = [0]),
         'throttle': pd.Series(data = [0]),
         'break':  pd.Series(data = [0])}

data = pd.DataFrame(items)


#--- pandas code ended ---#


while True :
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
      if keys[pygame.K_w]:
         image = pyautogui.screenshot()
         image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
         path = "photos/%d.png"%count
         cv2.imwrite(path, image)
         print("w is pressed ")
         count = count+ 1

      elif keys[pygame.K_q]:
         image = pyautogui.screenshot()
         image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
         path = "photos/%d.png"%count
         cv2.imwrite(path, image)
         print("q is pressed ")
         count = count+ 1

      elif keys[pygame.K_a]:
         image = pyautogui.screenshot()
         image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
         path = "photos/%d.png"%count
         cv2.imwrite(path, image)
         print("a is pressed ")
         count = count+ 1

      elif keys[pygame.K_s]:
         image = pyautogui.screenshot()
         image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
         path = "photos/%d.png"%count
         cv2.imwrite(path, image)
         print("s is pressed ")
         count = count+ 1

      elif keys[pygame.K_d]:
         image = pyautogui.screenshot()
         path = "photos/%d.png"%count
         cv2.imwrite(path, image)
         cv2.imwrite("photos/%d.png"%count, image)
         print("d is pressed ")
         count = count+ 1
         
      time.sleep(0.01)
      