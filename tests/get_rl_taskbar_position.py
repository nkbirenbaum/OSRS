import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from runelite import get_rl_taskbar_position

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
countdown(3)
position_focused = get_rl_taskbar_position(focused=True)
position_unfocused = get_rl_taskbar_position(focused=False)
print(position_focused)
print(position_unfocused)
print(f"Completed %s." % file_name)