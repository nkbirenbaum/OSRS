import pyautogui as pag
from functions import countdown
import os

print("Updating game window position in 3 seconds...")
countdown(3)
screenshot = pag.screenshot()
location = pag.locate("C:\Programming\OSRS\images\icons\\runelite.png", screenshot)
print(location)
x = location[0]
y = location[1]
os.environ['runelite_logo_x'] = str(584)
os.environ['runelite_logo_y'] = str(227)

print("Updated environment variables.")