import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import click_mouse

print("Executing test_click_mouse.py...")
time.sleep(0.5)
click_mouse('right')
print("Completed test_click_mouse.py.")