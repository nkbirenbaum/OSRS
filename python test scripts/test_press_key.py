import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from functions import press_key

print("Executing test_press_key.py...")
time.sleep(0.5)
countdown(3)
press_key('a')
print("Completed test_press_key.py.")