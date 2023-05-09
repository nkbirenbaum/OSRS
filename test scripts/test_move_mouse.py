import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import move_mouse
from functions import countdown

x_pos = 500
y_pos = 500
x_tol = 100
y_tol = 100

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
countdown(3)
move_mouse(x_pos, y_pos, x_tol, y_tol, delay_after=1.1)
move_mouse(x_pos, y_pos, x_tol, y_tol, delay_after=1.1, relative_to_rl=False)
print(f"Completed %s." % file_name)