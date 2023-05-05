import pyautogui as pag
import random
import numpy as np
import time
from scipy import interpolate
import math
import winsound
import os
from dotenv import set_key
from dotenv import load_dotenv

pag.MINIMUM_DURATION = 0 # Default: 0.1, any duration less than this is rounded to 0.0 to instantly move the mouse
pag.MINIMUM_SLEEP = 0    # Default: 0.05, minimal number of seconds to sleep between mouse moves
pag.PAUSE = 0            # Default: 0.1, the number of seconds to pause after EVERY public function call

def move_mouse(x_end=0, y_end=0, x_tol=0, y_tol=0, acceleration=True, relative=False):
    
    # Adjust endpoints if mouse movement is relative
    if relative:
        x_start, y_start = pag.position()
        x_end += x_start
        y_end += y_start

    # Adjust tolerances if potentially out of bounds
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
    cp = random.randint(3, 5)
    cp_x = np.linspace(x_start, x_end, num=cp, dtype='int')
    cp_y = np.linspace(y_start, y_end, num=cp, dtype='int')

    # Randomize inner control points a bit (+/-randomness at most)
    randomness = int(distance/15)
    cp_x_offset = [random.randint(-randomness, randomness) for k in range(cp)]
    cp_y_offset = [random.randint(-randomness, randomness) for k in range(cp)]
    cp_x_offset[0] = 0
    cp_x_offset[-1] = 0
    cp_y_offset[0] = 0
    cp_y_offset[-1] = 0
    cp_x += cp_x_offset
    cp_y += cp_y_offset

    # Approximate using Bezier spline (degree must be < # of cp)
    degree = 3 if cp > 3 else cp - 1
    tck, u = interpolate.splprep([cp_x, cp_y], k=degree)
    n_points = 1 + int(distance/20.0)
    if acceleration:
        u_temp = np.sqrt(np.linspace(0, 1, num=n_points))
        u_right = np.add(np.divide(u_temp, 2), 0.5)
        u_temp2 = np.subtract(1, np.flip(np.delete(u_temp, 0)))
        u_left = np.divide(np.abs(u_temp2), 2)
        u = np.concatenate((u_left, u_right))
    else:
        u = np.linspace(0, 1, num=n_points)
    points = interpolate.splev(u, tck)
    point_list=zip(*(i.astype(int) for i in points))

    # Timing of mouse movement
    duration = 0.040 + distance*(1+random.random())/6000
    timeout = duration / len(points[0])

    # Move mouse
    for point in point_list:
        pag.moveTo(*point)
        time.sleep(timeout)

    # Print new mouse coordinates
    load_dotenv()
    flag_debug_mouse_position = int(os.environ.get('FLAG_DEBUG_MOUSE_POSITION'))
    if flag_debug_mouse_position:
        print(f"Mouse moved to (%i, %i)." % (x_end, y_end))


# Presses given key with random duration
def press_key(key=''):
    
    # Randomize duration
    mu = 0.090
    sigma = 0.020
    d = 0
    while d < 0.030:
        d = random.gaussian(mu, sigma)

    # Press key with duration
    pag.keyDown(key)
    time.sleep(d)
    pag.keyUp(key)


# Clicks left mouse button with random duration
def click_mouse(button='left'):

    # Randomize duration
    mu = 0.050
    sigma = 0.015
    d = 0
    while d < 0.025:
        d = random.gauss(mu, sigma)
    
    # Click mouse with duration
    pag.mouseDown(button=button)
    time.sleep(d)
    pag.mouseUp(button=button)

    # Print new mouse coordinates
    load_dotenv()
    flag_debug_mouse_click = int(os.environ.get('FLAG_DEBUG_MOUSE_CLICK'))
    if flag_debug_mouse_click:
        print(f"Mouse click (%s)." % (button))


# Delay for a random short period between actions
def action_delay():

    mu = 0.030
    sigma = 0.015
    d = 0
    while d < 0.010:
        d = random.gaussian(mu, sigma)
    time.sleep(d)


# Countdown for a given number of seconds with sound cues
def countdown(iterations=3):
    
    iterations = int(iterations)
    frequency = 1000
    frequency2 = 1500
    duration = 200
    duration2 = 400
    for k in range(iterations):
        winsound.Beep(frequency, duration)
        time.sleep(0.8)
    winsound.Beep(frequency2, duration2)


# Updates the X and Y coordinates of the RuneLite window
def update_runelite_window_position():

    # Locate position of RuneLite window logo
    try:
        runelite_icon_file = os.getcwd() + "\images\icons\\runelite.png"
        location = pag.locateOnScreen(runelite_icon_file)
        x = location[0]
        y = location[1]
    except:
        print("Error: Could not locate RuneLite window in update_runelite_window_position()")
        return 0

    # Sets environment variables
    dotenv_path = os.getcwd() + "\.env"
    set_key(dotenv_path, 'RUNELITE_WINDOW_X', str(x))
    set_key(dotenv_path, 'RUNELITE_WINDOW_Y', str(y))
    print(f"RuneLite window postion updated to (%i, %i) in .env." % (x, y))


# Capture specified area of the screen
def capture_screen(area="all"):
    
    match area:
        case "all":
            im = pag.screenshot()
        case "runelite":
            im = pag.screenshot()
        case _:
            im = 0
            print("Error in capture_screen().", area, " is not a recognized area.")
    return im



# def scan_inventory():
    # Define here