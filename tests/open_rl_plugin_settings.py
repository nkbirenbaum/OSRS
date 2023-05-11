import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from runelite import focus_rl_window
from runelite import open_rl_plugin_settings

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
focus_rl_window()
open_rl_plugin_settings('NPC Indicators')
print(f"Completed %s." % file_name)