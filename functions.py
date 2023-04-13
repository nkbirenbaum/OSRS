import pyautogui as pag
import random
import numpy as np
import time
from scipy import interpolate
import math
import mouse

pag.MINIMUM_DURATION = 0 # Default: 0.1, any duration less than this is rounded to 0.0 to instantly move the mouse
pag.MINIMUM_SLEEP = 0    # Default: 0.05, minimal number of seconds to sleep between mouse moves
pag.PAUSE = 0            # Default: 0.1, the number of seconds to pause after EVERY public function call

# move_mouse_to function based on https://stackoverflow.com/questions/44467329/pyautogui-mouse-movement-with-bezier-curve
def move_mouse_to(x_end=0, y_end=0, x_tol=0, y_tol=0):
    
    # Adjust tolerance if potentially out of bounds
    screen_width, screen_height = pag.size()
    if x_end + x_tol > screen_width:
        x_tol = screen_width-x_end-1
    elif x_end - x_tol < 0:
        x_tol = x_end
    if y_end + y_tol > screen_height:
        y_tol = screen_height-y_end-1
    elif y_end - y_tol < 0:
        y_tol = y_end

    # Define line start, end, & total distance
    x_start, y_start = pag.position()
    x_end = x_end + random.randint(-x_tol, x_tol)
    y_end = y_end + random.randint(-y_tol, y_tol)
    distance = math.sqrt((x_end - x_start) ** 2 + (y_end - y_start) ** 2)

    # Distribute control points between start and destination evenly
    cp = random.randint(3, 5) # Number of bezier curve control points (must be at least 2)
    x = np.linspace(x_start, x_end, num=cp, dtype='int')
    y = np.linspace(y_start, y_end, num=cp, dtype='int')

    # Randomise inner control points a bit (+/-randomness at most)
    randomness = 40
    xr = [random.randint(-randomness, randomness) for k in range(cp)]
    yr = [random.randint(-randomness, randomness) for k in range(cp)]
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline
    degree = 3 if cp > 3 else cp - 1  # Degree of b-spline must be < # of control points
    tck, u = interpolate.splprep([x, y], k=degree)
    # Move up to a certain number of points
    u = np.linspace(0, 1, num=2+int(distance/10.0))
    points = interpolate.splev(u, tck)

    # Move mouse
    duration = 0.4
    timeout = duration / len(points[0])
    point_list=zip(*(i.astype(int) for i in points))
    print("List:", point_list)
    for point in point_list:
        pag.moveTo(*point)
        time.sleep(timeout)