# This test moves the cursor to random locations

import os
from time import sleep
import pyautogui as pag
import numpy as np

# Check your screen size
print(pag.size())

count=0
while count<10:
     x=np.random.randint(1,1792)
     y=np.random.randint(1,1120)
     pag.moveTo(x, y)
     print(x)
     print(y)
     sleep(1)
     count+=1

print(os.path.basename(__file__), "complete\n")