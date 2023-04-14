import pyautogui as pag
import time
from functions import move_mouse
from functions import press_key
from functions import click_mouse
from functions import action_delay

# Opens spellbook
def open_spellbook():

    press_key('f6')
    print("Spellbook opened.")

# Casts lumbridge home teleport
def cast_lumbridge_home_teleport():

    open_spellbook()
    action_delay()
    move_mouse(1535, 484, 15, 15)
    action_delay()
    click_mouse()
    time.sleep(11)