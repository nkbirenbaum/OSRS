import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from functions import get_skill_level

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
time.sleep(0.5)
countdown(3)
skill_name = 'hitpoints'
(level_cur, level_max) = get_skill_level(skill_name)
print(f"%s: %i / %i" % (skill_name, level_cur, level_max))
print(f"Completed %s." % file_name)