import sys
import os
import time
import datetime
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from runelite import focus_rl_window
from functions import capture_screen

script_name = os.path.basename(__file__)
print(f"Executing %s..." % script_name)
time.sleep(0.5)
focus_rl_window()
save_screen('runelite_sidebar')
print(f"Completed %s." % script_name)