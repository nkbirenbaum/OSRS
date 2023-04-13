import pyautogui as pag
import random
import numpy as np
import time
from scipy import interpolate
import math

pag.MINIMUM_DURATION = 0 # Default: 0.1, any duration less than this is rounded to 0.0 to instantly move the mouse
pag.MINIMUM_SLEEP = 0    # Default: 0.05, minimal number of seconds to sleep between mouse moves
pag.PAUSE = 0            # Default: 0.1, the number of seconds to pause after EVERY public function call

# move_mouse_to function based on https://stackoverflow.com/questions/44467329/pyautogui-mouse-movement-with-bezier-curve
def move_mouse_to(x_end=0, y_end=0):
    
    # Distance between 2 points
    def point_dist(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Distribute control points between start and destination evenly
    x_start, y_start = pag.position()
    cp = random.randint(3, 5) # Number of bezier curve control points (must be at least 2)
    x = np.linspace(x_start, x_end, num=cp, dtype='int')
    y = np.linspace(y_start, y_end, num=cp, dtype='int')

    # Randomise inner points a bit (+/-randomness at most)
    randomness = 10
    xr = [random.randint(-randomness, randomness) for k in range(cp)]
    yr = [random.randint(-randomness, randomness) for k in range(cp)]
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline
    degree = 3 if cp > 3 else cp - 1  # Degree of b-spline must be < # of control points
    tck, u = interpolate.splprep([x, y], k=degree)
    # Move up to a certain number of points
    u = np.linspace(0, 1, num=2+int(point_dist(x_start, y_start, x_end, y_end)/50.0))
    points = interpolate.splev(u, tck)

    # Move mouse
    pag.mouseDown()
    duration = 0.1
    timeout = duration / len(points[0])
    point_list=zip(*(i.astype(int) for i in points))
    for point in point_list:
        pag.moveTo(*point)
        time.sleep(timeout)
    pag.mouseUp()