import pyautogui as pag
import time
from functions import move_mouse

n_lines = 10
x_start = 300
y_start = 500
x_end = x_start + 1000
y_end = y_start + 0

print("Drawing lines in 3 seconds...")
time.sleep(3)
print("Drawing...")

for x in range(n_lines):
    move_mouse(x_start, y_start)
    pag.mouseDown()
    move_mouse(x_end, y_end, 5, 5)
    pag.mouseUp()

print("Drawing complete.")