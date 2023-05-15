import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from functions import mask_screen

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
countdown(3)
mask_screen(area='game', color=(0, 255, 255))
print(f"Completed %s." % file_name)