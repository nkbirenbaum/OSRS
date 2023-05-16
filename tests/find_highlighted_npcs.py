import sys
import os
import time
import cv2
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from functions import find_highlighted_npcs

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
countdown(3)
find_highlighted_npcs()
print(f"Completed %s." % file_name)