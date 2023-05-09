import sys
import os
import time
import datetime
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import countdown
from functions import capture_screen

script_name = os.path.basename(__file__)
print(f"Executing %s..." % script_name)
time.sleep(0.5)
countdown(3)
img = capture_screen('runelite_extended')
image_file = os.path.join(os.getcwd(), 'images', datetime.datetime.now().strftime("screenshot_%m%d%Y_%I%M%S.png"))
img.save(image_file)
print(f"Screenshot of RuneLite window saved to %s" % (image_file))
print(f"Completed %s." % script_name)