import os
import pyautogui as pag
import random
import numpy as np
import time
from scipy import interpolate
import math

pag.MINIMUM_DURATION = 0  # Default: 0.1, any duration less than this is rounded to 0.0 to instantly move the mouse.
pag.MINIMUM_SLEEP = 0  # Default: 0.05, minimal number of seconds to sleep between mouse moves.
pag.PAUSE = 0  # Default: 0.1, the number of seconds to pause after EVERY public function call.

def point_dist(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
#x1, y1 = pyautogui.position()  # Starting position
x1 = 200
y1 = 200
x2 = 800
y2 = 800

# Distribute control points between start and destination evenly.
x = np.linspace(x1, x2, num=cp, dtype='int')
y = np.linspace(y1, y2, num=cp, dtype='int')

# Randomise inner points a bit (+-RND at most).
RND = 10
xr = [random.randint(-RND, RND) for k in range(cp)]
yr = [random.randint(-RND, RND) for k in range(cp)]
xr[0] = yr[0] = xr[-1] = yr[-1] = 0
x += xr
y += yr

# Approximate using Bezier spline.
degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
                                  # Must be less than number of control points.
tck, u = interpolate.splprep([x, y], k=degree)
# Move upto a certain number of points
u = np.linspace(0, 1, num=2+int(point_dist(x1,y1,x2,y2)/50.0))
points = interpolate.splev(u, tck)

# Move mouse.
pag.moveTo(x1, y1)
pag.mouseDown()
duration = 0.1
timeout = duration / len(points[0])
point_list=zip(*(i.astype(int) for i in points))
for point in point_list:
    pag.moveTo(*point)
    time.sleep(timeout)
pag.mouseUp()

print(os.path.basename(__file__), "complete\n")