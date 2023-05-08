import sys
import os
from dotenv import load_dotenv
from functions import move_mouse
from functions import click_mouse
from functions import press_key
from functions import type_string

def open_rl_configuration():

    load_dotenv()
    runelite_window_x = int(os.environ.get('RUNELITE_WINDOW_X'))
    runelite_window_y = int(os.environ.get('RUNELITE_WINDOW_y'))
    w = 809
    h = 534


    return 1

def highlight_npc(npc_name):



    return 1