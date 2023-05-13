# Main script used to run sets of other functions

# Import libraries
import os
import subprocess
import pyautogui as pag
import sys

# Check if RuneLite is open
img_rl_unfocused = os.path.join(os.getcwd(), 'images', 'runelite', 'rl unfocused.png')
rl_unfocused = bool(pag.locateOnScreen(img_rl_unfocused, region=(0, 1030, 1920, 50), confidence=0.9))
img_rl_focused = os.path.join(os.getcwd(), 'images', 'runelite', 'rl focused.png')
rl_focused = bool(pag.locateOnScreen(img_rl_focused, region=(0, 1030, 1920, 50), confidence=0.9))

# Open RuneLite if not already open
if not(rl_unfocused) and not(rl_unfocused):
    rl_path = r"C:\Users\Nathan Birenbaum\AppData\Local\RuneLite\RuneLite.exe"
    # subprocess.call(rl_path, shell=False)

    # os.startfile(rl_path)
    sys.stdout = open(os.devnull, "w")
    sys.stderr = open(os.devnull, "w")
    subprocess.run(rl_path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW)
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    print("file started")