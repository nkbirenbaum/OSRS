import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import update_runelite_window_position
from functions import countdown

print("Executing test_update_runelite_window_position.py...")
time.sleep(0.5)
countdown(3)
update_runelite_window_position()
print("Completed test_update_runelite_window_position.py.")