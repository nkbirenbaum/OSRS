import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import move_mouse

x_pos = 500
y_pos = 500
x_tol = 100
y_tol = 100

print("Executing test_move_mouse.py...")
time.sleep(0.5)
move_mouse(x_pos, y_pos, x_tol, y_tol)
print("Completed test_move_mouse.py.")