import pyautogui as pag
import datetime
from functions import countdown

print("Taking screenshot in 3 seconds...")
countdown(3)
file_name = datetime.datetime.now().strftime("images\screenshot_%m%d%Y_%I%M%S.png")
screenshot = pag.screenshot()
location = pag.locate("C:\Programming\OSRS\images\icons\\runelite.png", screenshot)
x = location[0]
y = location[1]+24
w = 1096
h = 586
box = (x, y, w, h)
runelite_window = screenshot.crop(box)
runelite_window.save(file_name)
print("Screenshot saved as ", file_name, ".")