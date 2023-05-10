import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from functions import get_mouse_coordinates

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
countdown(3)
(rel_x, rel_y) = get_mouse_coordinates(relative=True)
print(f"Mouse position (RuneLite): (%i, %i)" % (rel_x, rel_y))
print(f"Completed %s." % file_name)