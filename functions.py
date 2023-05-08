import pyautogui as pag
import random
import numpy as np
import time
from scipy import interpolate
import math
import winsound
import os
import cv2
# from pytesseract import image_to_string
import pytesseract
from dotenv import set_key
from dotenv import load_dotenv

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" # Desktop tesseract path


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
        d = random.gauss(mu, sigma)

    # Press key with duration
    pag.keyDown(key)
    time.sleep(d)
    pag.keyUp(key)


# Clicks mouse button with random duration
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
        d = random.gauss(mu, sigma)
    time.sleep(d)


# Countdown for a given number of seconds with sound cues
def countdown(iterations=3):
    
    iterations = int(iterations)
    frequency = 1000
    frequency2 = 1500
    duration = 200
    duration2 = 400
    for k in range(iterations):
        print(iterations-k)
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
def capture_screen(area='all'):
    
    match area:
        case 'all':
            im = pag.screenshot()
        case 'runelite':
            load_dotenv()
            x = int(os.environ.get('RUNELITE_WINDOW_X'))
            y = int(os.environ.get('RUNELITE_WINDOW_y'))
            w = 809
            h = 534
            im = pag.screenshot(region=(x, y, w, h))
        case 'all_regions':
            load_dotenv()
            x = int(os.environ.get('RUNELITE_WINDOW_X')) + 4
            y = int(os.environ.get('RUNELITE_WINDOW_y')) + 27
            w = 809 - 40 - 4
            h = 534 - 27 - 4
            im = pag.screenshot(region=(x, y, w, h))
        case 'game':
            load_dotenv()
            x = int(os.environ.get('RUNELITE_WINDOW_X')) + 8
            y = int(os.environ.get('RUNELITE_WINDOW_y')) + 31
            w = 512
            h = 334
            im = pag.screenshot(region=(x, y, w, h))
        case 'chat':
            load_dotenv()
            x = int(os.environ.get('RUNELITE_WINDOW_X')) + 4
            y = int(os.environ.get('RUNELITE_WINDOW_y')) + 365
            w = 520
            h = 165
            im = pag.screenshot(region=(x, y, w, h))
        case 'minimap':
            load_dotenv()
            x = int(os.environ.get('RUNELITE_WINDOW_X')) + 520
            y = int(os.environ.get('RUNELITE_WINDOW_y')) + 27
            w = 249
            h = 168
            im = pag.screenshot(region=(x, y, w, h))
        case 'interface':
            load_dotenv()
            x = int(os.environ.get('RUNELITE_WINDOW_X')) + 526
            y = int(os.environ.get('RUNELITE_WINDOW_y')) + 195
            w = 241
            h = 335
            im = pag.screenshot(region=(x, y, w, h))
        case _:
            im = 0
            print("Error in capture_screen().", area, " is not a recognized area.")
    return im


# Returns specified skill level
def get_skill_level(skill='attack', currentOrMax='current'):

    # Get position for skill
    skill = skill.lower()
    x1 = 0
    y1 = 0
    match skill:
        case 'attack':
            # position = (27, 39, 60, 30)
            x1 = 27
            y1 = 39
        case 'strength':
            # position = (27, 71, 60, 30)
            x1 = 27
            y1 = 71
        case 'defence':
            # position = (27, 103, 60, 30)
            x1 = 27
            y1 = 103
        case 'ranged':
            # position = (27, 135, 60, 30)
            x1 = 27
            y1 = 135
        case 'prayer': 
            # position = (27, 167, 60, 30)
            x1 = 27
            y1 = 167
        case 'magic':
            # position = (27, 199, 60, 30)
            x1 = 27
            y1 = 199
        case 'runecraft':
            # position = (27, 231, 60, 30)
            x1 = 27
            y1 = 231
        case 'construction':
            # position = (27, 263, 60, 30)
            x1 = 27
            y1 = 263
        case 'hitpoints':
            # position = (90, 39, 60, 30)
            x1 = 90
            y1 = 39
        case 'agility':
            # position = (90, 71, 60, 30)
            x1 = 90
            y1 = 71
        case 'herblore':
            # position = (90, 103, 60, 30)
            x1 = 90
            y1 = 103
        case 'theiving':
            # position = (90, 135, 60, 30)
            x1 = 90
            y1 = 135
        case 'crafting': 
            # position = (90, 167, 60, 30)
            x1 = 90
            y1 = 167
        case 'fletching':
            # position = (90, 199, 60, 30)
            x1 = 90
            y1 = 199
        case 'slayer':
            # position = (90, 231, 60, 30)
            x1 = 90
            y1 = 231
        case 'hunting':
            # position = (90, 263, 60, 30)
            x1 = 90
            y1 = 263
        case 'mining':
            # position = (153, 39, 60, 30)
            x1 = 153
            y1 = 39
        case 'smithing':
            # position = (153, 71, 60, 30)
            x1 = 153
            y1 = 71
        case 'fishing':
            # position = (153, 103, 60, 30)
            x1 = 153
            y1 = 103
        case 'cooking':
            # position = (153, 135, 60, 30)
            x1 = 153
            y1 = 135
        case 'firemaking': 
            # position = (153, 167, 60, 30)
            x1 = 153
            y1 = 167
        case 'woodcutting':
            # position = (153, 199, 60, 30)
            x1 = 153
            y1 = 199
        case 'farming':
            # position = (153, 231, 60, 30)
            x1 = 153
            y1 = 231
        case 'total':
            # position = (153, 263, 60, 30)
            x1 = 153
            y1 = 263
        case _:
            print("Error in get_skill_level().", skill, " is not a recognized skill.")
            return 0
    x2 = x1 + 60
    y2 = y1 + 30

    # Capture skill interface & extract portion corresponding to skill
    press_key('f2')
    img_all_skills = capture_screen(area='interface')
    img_skill = img_all_skills.crop((x1, y1, x2, y2))
    # img_skill.show()

    # Convert to OpenCV format
    # img_cv = cv2.cvtColor(np.array(img_skill), cv2.COLOR_BGR2RGB)
    # img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    # img_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV)[1]
    # cv2.imshow("Test image", img_gray)
    # cv2.waitKey(0)
    # img_text = pytesseract.image_to_string(img_threshold, config="--psm 7")
    # print(img_text)
    # # print("".join([t for t in txt if t != '|']).strip())

    img_cv = cv2.cvtColor(np.array(img_skill), cv2.COLOR_BGR2HSV)
    # lower = np.array([35, 235, 20]) 
    # upper = np.array([45, 245, 255])
    img_mask = cv2.inRange(img_cv, (15, 0, 0), (100, 255, 255))

    # img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    # img_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Image mask", img_mask)
    cv2.waitKey(0)
    # img_text = pytesseract.image_to_string(img_threshold, config="--psm 7")
    # print(img_text)
    # print("".join([t for t in txt if t != '|']).strip())
    
    # cv2.imshow("Test image", im_cv)
    # cv2.waitKey(0)

    level = 0
    return level