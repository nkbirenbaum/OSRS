import pyautogui as pag
import datetime
from functions import countdown

file_name = datetime.datetime.now().strftime("images\screenshot_%m%d%Y_%I%M%S.png")
print("Taking screenshot in 3 seconds...")
countdown(3)
pag.screenshot(file_name)
print("Screenshot saved as ", file_name, ".")