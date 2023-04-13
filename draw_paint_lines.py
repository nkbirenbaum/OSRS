import pyautogui as pag
import time
from functions import move_mouse_to

n_lines = 10
x_start = 300
y_start = 200
#x_end = 1200
#y_end = 800
x_end = 400
y_end = 300

print("Drawing lines in 3 seconds...")
time.sleep(3)
print("Drawing...")

for x in range(n_lines):
    move_mouse_to(x_start, y_start)
    pag.mouseDown()
    move_mouse_to(x_end, y_end, 20, 20)
    pag.mouseUp()
    print("-------------")

print("Drawing complete.")