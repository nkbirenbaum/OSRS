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
os.environ['RUNELITE_POS_X'] = str(x)
os.environ['RUNELITE_POS_Y'] = str(y)

print("Updated environment variables.")