import pyautogui as pag
from functions import countdown

from spellbook import cast_lumbridge_home_teleport

print("Casting lumbridge teleport in 3 seconds...")
countdown(3)
cast_lumbridge_home_teleport()
print("Complete.")