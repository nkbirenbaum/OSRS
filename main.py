# Main script used to run sets of other functions

# Import libraries
import os
import subprocess
import sys
import time
import pyautogui as pag
from runelite import *
from functions import *

# Open RuneLite and update the window position
open_rl()
focus_rl_window()
update_rl_window_position()