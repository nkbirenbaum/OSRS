import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from functions import capture_screen

print("Executing test_capture_screen_interface.py...")
time.sleep(0.5)
countdown(3)
im = capture_screen('interface')
im.show()
print("Completed test_capture_screen_interface.py.")