import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown

print("Executing test_countdown.py...")
time.sleep(0.5)
countdown(3)
print("Completed test_countdown.py.")