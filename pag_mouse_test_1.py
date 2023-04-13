# This test draws a spiral slowly (~18s)

import time
import pyautogui as pag

pag.MINIMUM_DURATION = 0
pag.MINIMUM_SLEEP = 0
pag.PAUSE = 0

pag.moveTo(500, 500, 0.5) # Move the mouse to XY coordinates.

start_time = time.time()
line_duration = 0.5
distance = 200
while distance > 0:
    pag.drag(distance, 0, duration=line_duration, _pause=False)   # move right
    distance -= 20
    pag.drag(0, distance, duration=line_duration, _pause=False)   # move down
    pag.drag(-distance, 0, duration=line_duration, _pause=False)  # move left
    distance -= 20
    pag.drag(0, -distance, duration=line_duration, _pause=False)  # move up
end_time = time.time()

print(end_time-start_time)