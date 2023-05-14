import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from functions import countdown
from functions import get_mouse_coordinates
colorama_init()

# Begin script execution
file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)

# Get mouse coordinates twice
countdown(3)
(abs_x1, abs_y1) = get_mouse_coordinates(relative=False)
(rel_x1, rel_y1) = get_mouse_coordinates(relative=True)
countdown(3)
(abs_x2, abs_y2) = get_mouse_coordinates(relative=False)
(rel_x2, rel_y2) = get_mouse_coordinates(relative=True)

# Calculate x_end, y_end, x_tol, & y_tol for absolute & relative positions
w = abs_x2 - abs_x1
h = abs_y2 - abs_y1
x_tol = int(w/2 - 1)
y_tol = int(h/2 - 1)
x_abs = round(abs_x1 + w/2)
y_abs = round(abs_y1 + h/2)
x_rel = round(rel_x1 + w/2)
y_rel = round(rel_y1 + h/2)

# Print mouse data
print(f"Mouse position (absolute): {Fore.GREEN}(x_end=%i, y_end=%i, x_tol=%i, y_tol=%i){Style.RESET_ALL}" % (x_abs, y_abs, x_tol, y_tol))
print(f"Mouse position (RuneLite): {Fore.GREEN}(x_end=%i, y_end=%i, x_tol=%i, y_tol=%i){Style.RESET_ALL}" % (x_rel, y_rel, x_tol, y_tol))
print(f"Completed %s." % file_name)