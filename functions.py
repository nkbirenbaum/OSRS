import pyautogui as pag
import random
import numpy as np
import time
import math
import winsound
import os
import cv2
import pytesseract
import platform
from dotenv import load_dotenv
from scipy import interpolate

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" # Path to tesseract.exe

pag.MINIMUM_DURATION = 0 # Default: 0.1, any duration less than this is rounded to 0.0 to instantly move the mouse
pag.MINIMUM_SLEEP = 0    # Default: 0.05, minimal number of seconds to sleep between mouse moves
pag.PAUSE = 0            # Default: 0.1, the number of seconds to pause after EVERY public function call

# Prints current mouse coordinates
def get_mouse_coordinates(relative=True):

    # Get RuneLite window position
    load_dotenv()
    runelite_window_x = int(os.environ.get('RUNELITE_WINDOW_X'))
    runelite_window_y = int(os.environ.get('RUNELITE_WINDOW_y'))

    # Get & print current & relative mouse positions
    (x, y) = pag.position()
    if relative:
        x -= runelite_window_x
        y -= runelite_window_y

    return (x, y)


def move_mouse(x_end=0, y_end=0, x_tol=0, y_tol=0, delay_after=0, acceleration=True, relative_to_rl=True):
    
    # Adjust endpoints if mouse movement is relative to RuneLite window
    load_dotenv()
    if relative_to_rl:
        runelite_window_x = int(os.environ.get('RUNELITE_WINDOW_X'))
        runelite_window_y = int(os.environ.get('RUNELITE_WINDOW_y'))
        x_end += runelite_window_x
        y_end += runelite_window_y

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
    flag_debug_mouse_position = int(os.environ.get('FLAG_DEBUG_MOUSE_POSITION'))
    if flag_debug_mouse_position:
        print(f"Mouse moved to (%i, %i)." % (x_end, y_end))

    # Delay afterwards
    if delay_after>0:
        action_delay(mu=delay_after)

    return 1


# Presses given key with random duration
def press_key(key='', delay_after=0):
    
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

    # Delay afterwards
    if delay_after>0:
        action_delay(mu=delay_after)

    return 1


# Presses given key combo with random duration
def press_keys(key1='', key2='', delay_after=0):
    
    # Randomize duration
    mu = 0.090
    sigma = 0.020
    d1 = 0
    while d1 < 0.030:
        d1 = random.gauss(mu, sigma)
    d2 = 0
    while d2 < 0.030:
        d2 = random.gauss(mu, sigma)
    d3 = 0
    while d3 < 0.030:
        d3 = random.gauss(mu, sigma)

    # Press key with duration
    pag.keyDown(key1)
    time.sleep(d1)
    pag.keyDown(key2)
    time.sleep(d2)
    pag.keyUp(key2)
    time.sleep(d3)
    pag.keyUp(key1)

    # Delay afterwards
    if delay_after>0:
        action_delay(mu=delay_after)

    return 1

# Types input string
def type_string(phrase='', delay_after=0):

    for ii in phrase:
        press_key(ii)

    # Delay afterwards
    if delay_after>0:
        action_delay(mu=delay_after)

    return 1


# Clicks mouse button with random duration
def click_mouse(button='left', delay_after=0):

    # Error if button is invalid
    button = button.lower()
    if button not in ('left', 'right', 'middle'):
        print(f"Error in click_mouse(): unrecognized button '%s'" % (button))
        return 0

    # Randomize click duration
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
        print(f"Mouse %s-click." % (button))

    # Delay afterwards
    if delay_after>0:
        action_delay(mu=delay_after)

    return 1


# Delay for a random short period between actions
def action_delay(mu=0.5, sigma=0.0, exact=False):

    # If 'exact', perform delay and return immediately
    if exact:
        time.sleep(mu)
        return 1
    
    # Sigma must be less than mu
    if sigma>mu:
        print(f"Error in action_delay(): input 'sigma' argument (%.3f) must be less than input 'mu' argument (%.3f)." % (sigma, mu))
        return 0        

    # Compare to minimum delay
    minimum_delay = 0.010
    if mu<minimum_delay:
        print(f"Error in action_delay(): input 'mu' argument must be at least %.3f" % minimum_delay)
        return 0
    
    # Calculate sigma if not given & not exact
    if not(exact) and sigma==0:
        sigma = mu/3

    # Find delay time 'd' and perform delay
    d = 0
    while d < minimum_delay:
        d = random.gauss(mu, sigma)
    time.sleep(d)

    return 1


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

    return 1


# Capture specified area of the screen
def capture_screen(area='all'):
    
    # Load window position from .env
    load_dotenv()
    x = int(os.environ.get('RUNELITE_WINDOW_X'))
    y = int(os.environ.get('RUNELITE_WINDOW_Y'))

    # Determine area to screenshot
    area = area.lower()
    match area:
        case 'all':
            img = pag.screenshot()
            return img
        case 'runelite':
            w = 809
            h = 534
        case 'runelite_extended':
            w = 1051
            h = 534
        case 'runelite_sidebar':
            x += 769
            w = 282
            h = 534
        case 'all_regions':
            x += 4
            y += 27
            w = 765
            h = 503
        case 'game':
            x += 8
            y += 31
            w = 512
            h = 334
        case 'chat':
            x += 4
            y += 365
            w = 520
            h = 165
        case 'minimap':
            x += 520
            y += 27
            w = 249
            h = 168
        case 'interface':
            x += 526
            y += 195
            w = 241
            h = 335
        case _:
            print(f"Error in capture_screen(): area '%s' is not recognized." % (area))
            return 0
    
    # Screenshot area
    img = pag.screenshot(region=(x, y, w, h))
    return img


# Returns specified skill level
def get_skill_level(skill='attack'):

    # Get position for skill
    skill = skill.lower()
    x1 = 0
    y1 = 0
    match skill:
        case 'attack':
            x1 = 27
            y1 = 39
        case 'strength':
            x1 = 27
            y1 = 71
        case 'defence':
            x1 = 27
            y1 = 103
        case 'ranged':
            x1 = 27
            y1 = 135
        case 'prayer': 
            x1 = 27
            y1 = 167
        case 'magic':
            x1 = 27
            y1 = 199
        case 'runecraft':
            x1 = 27
            y1 = 231
        case 'construction':
            x1 = 27
            y1 = 263
        case 'hitpoints':
            x1 = 90
            y1 = 39
        case 'agility':
            x1 = 90
            y1 = 71
        case 'herblore':
            x1 = 90
            y1 = 103
        case 'theiving':
            x1 = 90
            y1 = 135
        case 'crafting': 
            x1 = 90
            y1 = 167
        case 'fletching':
            x1 = 90
            y1 = 199
        case 'slayer':
            x1 = 90
            y1 = 231
        case 'hunting':
            x1 = 90
            y1 = 263
        case 'mining':
            x1 = 153
            y1 = 39
        case 'smithing':
            x1 = 153
            y1 = 71
        case 'fishing':
            x1 = 153
            y1 = 103
        case 'cooking':
            x1 = 153
            y1 = 135
        case 'firemaking': 
            x1 = 153
            y1 = 167
        case 'woodcutting':
            x1 = 153
            y1 = 199
        case 'farming':
            x1 = 153
            y1 = 231
        case _:
            print(f"Error in get_skill_level(): unrecognized input '%s' for 'skill' argument." % (skill))
            return 0
    x2 = x1 + 60
    y2 = y1 + 30

    # Capture skill interface & extract portion corresponding to skill
    press_key('f2')
    img_all_skills = capture_screen(area='interface')
    img_skill = img_all_skills.crop((x1, y1, x2, y2))

    # Convert to OpenCV format & mask yellow numbers
    img_cv = cv2.cvtColor(np.array(img_skill), cv2.COLOR_BGR2HSV)
    hsv_lower = np.array([89, 250, 250])
    hsv_upper = np.array([91, 255, 255])
    img_mask = cv2.inRange(img_cv, hsv_lower, hsv_upper)

    # Determine if current & minimum levels have 2 digits
    img_check_current_level_tens = img_mask[4:12, 34:36]
    img_check_maximum_level_tens = img_mask[16:24, 46:48]
    current_level_two_digits = True if img_check_current_level_tens.sum() > 0 else False
    maximum_level_two_digits = True if img_check_maximum_level_tens.sum() > 0 else False

    # Start and end cropping positions for current & maximum levels
    y1_c = 4
    y2_c = 12
    y1_m = 16
    y2_m = 24
    x1_c_1s = 36
    x2_c_1s = 41
    x1_m_1s = 48
    x2_m_1s = 53
    
    # Read numbers template file
    try:
        template_file = os.path.join(os.getcwd(), 'images', 'levels', '0123456789.png')
        template = cv2.imread(template_file, 0)
    except:
        print(f"Error in get_skill_level(): could not open template file '%s'." % (template_file))
        return 0

    # Get current level ones place values
    if current_level_two_digits:
        x1_c_1s += 2
        x2_c_1s += 2
    img_current_level_ones = img_mask[y1_c:y2_c, x1_c_1s:x2_c_1s]
    try:
        result = cv2.matchTemplate(img_current_level_ones, template, cv2.TM_CCOEFF)
        _, _, _, top_left = cv2.minMaxLoc(result)
        current_level_ones = top_left[0]/5
    except:
        current_level_ones = 0
        print(f"Error in get_skill_level(): could not find current '%s' level ones place." % (skill))

    # Get maximum level ones place values
    if maximum_level_two_digits:
        x1_m_1s += 2
        x2_m_1s += 2
    img_maximum_level_ones = img_mask[y1_m:y2_m, x1_m_1s:x2_m_1s]
    try:
        result = cv2.matchTemplate(img_maximum_level_ones, template, cv2.TM_CCOEFF)
        _, _, _, top_left = cv2.minMaxLoc(result)
        maximum_level_ones = top_left[0]/5
    except:
        maximum_level_ones = 0
        print(f"Error in get_skill_level(): could not find maximum '%s' level ones place." % (skill))

    # Get current level tens place values - TESTED 0-13 only
    current_level_tens = 0
    if current_level_two_digits:
        x1_c_10s = 34
        x2_c_10s = 39
        fat_num_list = [ 0, 2, 3, 5, 6, 7, 8, 9 ]
        if current_level_ones in fat_num_list:
            x1_c_10s -= 1
            x2_c_10s -= 1
        img_current_level_tens = img_mask[y1_c:y2_c, x1_c_10s:x2_c_10s]
        try:
            result = cv2.matchTemplate(img_current_level_tens, template, cv2.TM_CCOEFF)
            _, _, _, top_left = cv2.minMaxLoc(result)
            current_level_tens = top_left[0]/5
        except: 
            print(f"Error in get_skill_level(): could not find current '%s' level tens place." % (skill))
    
    # Get maximum level tens place values - TESTED 0-12 only
    maximum_level_tens = 0
    if maximum_level_two_digits:
        x1_m_10s = 46
        x2_m_10s = 51
        fat_num_list = [ 0, 2, 3, 5, 6, 7, 8, 9 ]
        if maximum_level_ones in fat_num_list:
            x1_m_10s -= 1
            x2_m_10s -= 1
        img_maximum_level_tens = img_mask[y1_m:y2_m, x1_m_10s:x2_m_10s]
        try:
            result = cv2.matchTemplate(img_maximum_level_tens, template, cv2.TM_CCOEFF)
            _, _, _, top_left = cv2.minMaxLoc(result)
            maximum_level_tens = top_left[0]/5
        except:
            print(f"Error in get_skill_level(): could not find maximum '%s' level tens place." % (skill))

    # Save images for later debugging of higher levels
    # cv2.imwrite("cur ones.png", img_current_level_ones)
    # cv2.imwrite("cur tens.png", img_current_level_tens)
    # cv2.imwrite("max ones.png", img_maximum_level_ones)
    # cv2.imwrite("max tens.png", img_maximum_level_tens)

    # Calculate current & maximum levels
    current_level = current_level_ones + 10*current_level_tens
    maximum_level = maximum_level_ones + 10*maximum_level_tens    

    return (current_level, maximum_level)


# Warn if not running specified operating system release
def check_os_version(os='Windows', release='10'):

    # Get current operating system & version
    current_os = platform.system()
    current_release = platform.release()

    # Compare to input operating system & version and warn if different
    if (os != current_os) or (release != current_release):
        print(f"Warning: This script was designed for %s %s. Current operating system is %s %s. Some functions may not work properly." % (os, release, current_os, current_os, current_release))
    return 1


# Next function
def standardize_view():

    # Look North
    move_mouse(x_end=563, y_end=46, x_tol=10, y_tol=9, delay_after = 0.1)
    click_mouse(delay_after=0.4)

    # Reset zoom position (512)
    press_key('ctrlleft', delay_after=0.7)

    # Tilt until aerial view
    pag.keyDown('up')
    time.sleep(2.5 + abs(random.gauss(0.1, 0.4)))
    pag.keyUp('up')

    return 1


# Find cyan outline of images 
def mask_screen(area='all', color=(255, 255, 255)):

    # img_file = os.path.join(os.getcwd(), 'images', 'cyan.png')
    # img = cv2.imread(img_file)
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(img)
    # print(img_rgb)

    # Screenshot game and mask cyan NPC outline
    img_game = capture_screen(area='game')
    open_cv_image = np.array(img_game)
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    cv2.imshow("open_cv_image", open_cv_image)
    cv2.waitKey(0)

    img_hsv = cv2.cvtColor(np.array(img_game), cv2.COLOR_RGB2HSV)
    cv2.imshow("img_hsv", img_hsv)
    cv2.waitKey(0)


    lower = np.array([89, 250, 250])
    upper = np.array([91, 255, 255])
    img_mask = cv2.inRange(img_hsv, lower, upper)
    cv2.imshow("img_mask", img_mask)
    cv2.waitKey(0)
    # print(img_mask)
    result = cv2.bitwise_and(img_hsv, img_hsv, mask=img_mask)
    cv2.imshow("result", result)
    cv2.waitKey(0)