import numpy as np
import cv2
import pytesseract
import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from functions import press_key
from functions import capture_screen

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" # Path to tesseract.exe

# See: https://groups.google.com/g/tesseract-ocr/c/Wdh_JJwnw94/m/24JHDYQbBQAJ

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
            print("Error in get_skill_level().", skill, " is not a recognized skill.")
            return 0
    x2 = x1 + 60
    y2 = y1 + 30

    # Capture skill interface & extract portion corresponding to skill
    press_key('f2')
    img_all_skills = capture_screen(area='interface')
    img_skill = img_all_skills.crop((x1, y1, x2, y2))

    # Convert to OpenCV format & mask
    img_cv = cv2.cvtColor(np.array(img_skill), cv2.COLOR_BGR2HSV)
    hsv_lower = np.array([89, 250, 250])
    hsv_upper = np.array([91, 255, 255])
    img_mask = cv2.inRange(img_cv, hsv_lower, hsv_upper)

    # Crop areas for current & maximum levels
    img_cur_level = img_mask[3:13, 30:44]
    img_max_level = img_mask[15:25, 42:56]
    scale_percent = 300
    width = int(img_cur_level.shape[1] * scale_percent / 100)
    height = int(img_cur_level.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_cur_level = cv2.resize(img_cur_level, dim, interpolation = cv2.INTER_AREA)
    img_max_level = cv2.resize(img_max_level, dim, interpolation = cv2.INTER_AREA)
    kernel = np.ones((2,2), np.uint8)
    img_cur_level = cv2.dilate(img_cur_level, kernel, iterations=1)
    cv2.imshow("Current", img_cur_level)
    cv2.waitKey(0)
    cv2.imshow("Max", img_max_level)
    cv2.waitKey(0)

    # Extract text of levels
    # config_options = "--psm 8 --oem 3 digits" # 7 single line, 8 single word, 10 single char tessedit_char_whitelist=0123456789
    config_options = "--psm 13 --oem 3 digits"
    text_cur = pytesseract.image_to_string(img_cur_level, config=config_options)
    try:
        level_cur = int(text_cur)
    except:
        level_cur = 0
        print(f"Current %s level not recognized. OCR result: %s" % (skill, text_cur))
    text_max = pytesseract.image_to_string(img_max_level, config=config_options)
    try:
        level_max = int(text_max)
    except:
        level_max = 0
        print(f"Maximum %s level not recognized. OCR result: %s" % (skill, text_max))

    return (level_cur, level_max)