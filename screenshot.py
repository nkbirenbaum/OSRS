import pyautogui as pag
import time

print("Taking screenshot in 3 seconds...")
time.sleep(3)
pag.screenshot("images\my_screenshot3.png")
print("Screenshot saved.")