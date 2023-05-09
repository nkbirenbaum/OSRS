import sys
import os
import time
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import action_delay

print("Executing test_action_delay.py...")
time.sleep(0.5)
action_delay()
action_delay(mu=0.5)
action_delay(mu=0.5, sigma=0.2)
action_delay(mu=0.5, sigma=0.2, exact=True)
action_delay(mu=0.5, sigma=0.2, exact=False)
action_delay(mu=0.5, sigma=0.7)
print("Completed test_action_delay.py.")