import sys
import os
import time
import datetime
import pyautogui as pag
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from runelite import focus_rl_window
from functions import capture_screen
from functions import countdown
from functions import click_mouse

script_name = os.path.basename(__file__)
print(f"Executing %s..." % script_name)
time.sleep(0.5)
focus_rl_window()
countdown(3)
click_mouse()

img_red_x = os.path.join(os.getcwd(), 'images', 'mouse', 'red x.png')
red_x = pag.locateOnScreen(img_red_x, confidence=0.9)
print(red_x)

print(f"Completed %s." % script_name)