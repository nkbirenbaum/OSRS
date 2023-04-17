import pyautogui as pag
import datetime
from functions import countdown

print("Updating game window position in 3 seconds...")
countdown(3)
screenshot = pag.screenshot()
location = pag.locate("C:\Programming\OSRS\images\icons\\runelite.png", screenshot)
x = location[0]
y = location[1]
settings_file_name = "settings\positions"
f = open("settings\positions", "w")
f.write("runelite_logo_x,")
f.write(str(x))
f.write("\n")
f.write("runelite_logo_y,")
f.write(str(y))
f.write("\n")
f.close()
print("Updated", settings_file_name)