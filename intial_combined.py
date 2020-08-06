import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui 
import pandas as pd 
import pygame 

from pygame.locals import *

dirName = "photos"
try:
    os.makedirs(dirName)    
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

while True:
   keys = pygame.key.get_pressed()
   for event in pygame.event.get():
      if keys[pygame.K_w]:
         print("w is pressed ")
      elif keys[pygame.K_q]:
         print("q is pressed ")
      elif keys[pygame.K_a]:
         print("a is pressed ")
      elif keys[pygame.K_s]:
         print("s is pressed ")
      elif keys[pygame.K_d]:
         print("d is pressed ")
      time.sleep(0.01)


image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", image)

items = {'Images' : pd.Series(data = [1]),
         'left_side': pd.Series(data = [1]),
         'right_side': pd.Series(data = [1]),
         'throttle': pd.Series(data = [1]),
         'break':  pd.Series(data = [1])}

data = pd.DataFrame(items)

# We display the DataFrame
data


d