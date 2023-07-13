import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from runelite import wait_login_screen

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
wait_login_screen(timeout=10)
print(f"Completed %s." % file_name)