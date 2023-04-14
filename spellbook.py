import pyautogui as pag
import time
import random
from functions import move_mouse

def open_spellbook():

    pag.keyDown('f6')
    d = 0.070 + 0.080*random.random()
    time.sleep(d)
    pag.keyUp('f6')
    print("Spellbook opened.")

def cast_lumbridge_home_teleport():

    open_spellbook()
    d = 0.010 + 0.050*random.random()
    move_mouse(1535, 484, 15, 15)
    pag.mouseDown()
    d = 0.070 + 0.030*random.random()
    time.sleep(d)
    pag.mouseUp()
    time.sleep(11)