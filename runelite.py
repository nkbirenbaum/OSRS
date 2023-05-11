import os
import pyperclip as pc
import pyautogui as pag
from dotenv import load_dotenv
from functions import move_mouse
from functions import click_mouse
from functions import press_keys
from functions import press_key
from functions import type_string


# Brings RuneLite window into focus if unfocused
def focus_rl_window():

    # Check whether RuneLite window is unfocused and focused
    img_rl_unfocused = os.path.join(os.getcwd(), 'images', 'runelite', 'rl unfocused.png')
    rl_unfocused = pag.locateOnScreen(img_rl_unfocused, region=(0, 1030, 1920, 50), confidence=0.9)
    img_rl_focused = os.path.join(os.getcwd(), 'images', 'runelite', 'rl focused.png')
    rl_focused = pag.locateOnScreen(img_rl_focused, region=(0, 1030, 1920, 50), confidence=0.9)

    # Maximize if minimized
    if not(bool(rl_focused)) and bool(rl_unfocused):
        x = rl_unfocused[0]
        y = rl_unfocused[1]
        w = rl_unfocused[2]
        h = rl_unfocused[3]
        move_mouse(x_end=int(x+w/2), y_end=int(y+h/2), x_tol=int(w/3), y_tol=int(h/3), delay_after=0.5, relative_to_rl=False)
        click_mouse(delay_after=0.5)
        print("RuneLite window focused.")
    else:
        print("Error in focus_rl_window(): RuneLite app not found in taskbar.")
        return 0
    
    return 1


# Opens RuneLite configuration sidebar
def open_rl_configuration():

    # Load window position from .env & define sidebar position
    load_dotenv()
    x = int(os.environ.get('RUNELITE_WINDOW_X'))
    y = int(os.environ.get('RUNELITE_WINDOW_Y'))
    w = 282
    h = 534

    # Check whether sidebar is already expanded
    img_sidebar_dash_x = os.path.join(os.getcwd(), 'images', 'runelite', 'sidebar dash x.png')
    sidebar_expanded = bool(pag.locateOnScreen(img_sidebar_dash_x, region=(x+809, y, w, h), confidence=0.9))

    # Check whether small configuration settings button is activated
    img_config_small_open = os.path.join(os.getcwd(), 'images', 'runelite', 'config small open.png')
    config_small_opened = bool(pag.locateOnScreen(img_config_small_open, region=(x+769, y, w, h), confidence=0.9))
    
    # Open sidebar & activate small configuration settings button
    if not(sidebar_expanded) and not(config_small_opened):
        move_mouse(x_end=785, y_end=40, x_tol=9, y_tol=9, delay_after=0.5)
        click_mouse(delay_after=0.5)
    elif sidebar_expanded and not(config_small_opened):
        move_mouse(x_end=1028, y_end=40, x_tol=9, y_tol=9, delay_after=0.5)
        click_mouse(delay_after=0.5)

    # Check whether large configuration settings button is activated
    img_config_large_open = os.path.join(os.getcwd(), 'images', 'runelite', 'config large open.png')
    config_large_opened = bool(pag.locateOnScreen(img_config_large_open, region=(x+769, y, w, h), confidence=0.9))

    # Activate large configuration button
    if not(config_large_opened):
        move_mouse(x_end=810, y_end=50, x_tol=10, y_tol=10, delay_after=0.5)
        click_mouse(delay_after=0.5)

    # Press back button if plugin configuration is already open
    img_config_back_button = os.path.join(os.getcwd(), 'images', 'runelite', 'config back button.png')
    plugin_config_opened = bool(pag.locateOnScreen(img_config_back_button, region=(x+770, y+70, 30, 30), confidence=0.9))
    if plugin_config_opened:
        move_mouse(x_end=786, y_end=89, x_tol=2, y_tol=3, delay_after=0.5)
        click_mouse(delay_after=0.5)

    print("RuneLite plugins configuration opened.")
    return 1


# Open plugin settings
def open_rl_plugin_settings(plugin_name=''):

    # Return if plugin_name is empty
    if plugin_name=='':
        print(f"Error in open_rl_plugin_settings(): 'plugin_name' argument cannot be empty.")
        return 0

    # Load window position from .env
    load_dotenv()
    rl_win_x = int(os.environ.get('RUNELITE_WINDOW_X'))
    rl_win_y = int(os.environ.get('RUNELITE_WINDOW_Y'))

    # Open RuneLite configuration & select search bar
    open_rl_configuration()
    move_mouse(x_end=870, y_end=98, x_tol=50, y_tol=5, delay_after=0.5)
    click_mouse(delay_after=0.5)

    # Clear search bar & type plugin name
    press_keys(key1='ctrlleft', key2='a', delay_after=0.5)
    press_key(key='delete', delay_after=0.5)
    type_string(phrase=plugin_name, delay_after=0.5)

    # Click plugins settings
    move_mouse(x_end=963, y_end=138, x_tol=4, y_tol=4, delay_after=0.5)
    click_mouse(delay_after=0.5)
    print(f"'%s' plugin configuration opened." % (plugin_name))

    # Enable plugin if disabled
    img_plugin_enabled = os.path.join(os.getcwd(), 'images', 'runelite', 'plugin enabled.png')
    plugin_enabled = pag.locateOnScreen(img_plugin_enabled, region=(rl_win_x+960, rl_win_y+70, 60, 40))
    if not(plugin_enabled):
        move_mouse(x_end=990, y_end=90, x_tol=4, y_tol=2, delay_after=0.3)
        click_mouse(delay_after=0.5)
        print(f"'%s' plugin enabled." % (plugin_name))
    return 1


# Highlight NPC
def highlight_npc(npc_name='', replace_or_append='replace'):

    # Return if npc_name is empty
    if npc_name=='':
        print(f"Error in highlight_npc(): npc_name argument cannot be empty.")
        return 0
    npc_name = npc_name.lower()

    # Return if replace_or_append is not 'append' or 'replace'
    replace_or_append = replace_or_append.lower()
    if replace_or_append!='append' and replace_or_append!='replace':
        print(f"Error in highlight_npc(): unrecognized input '%s' for 'replace_or_append' argument." % (replace_or_append))
        return 0

    # Open RuneLite configuration sidebar & NPC Indicators settings
    open_rl_plugin_settings('npc indicators')

    # Enter NPCs to highlight text box
    move_mouse(x_end=880, y_end=475, x_tol=5, y_tol=5, delay_after=0.5)
    click_mouse(delay_after=0.5)

    # Replace with new NPC name
    if replace_or_append=='replace':
        press_keys('ctrlleft', 'a', delay_after=0.5)
        press_key('delete', delay_after=0.5)
        type_string(phrase=npc_name, delay_after=0.5)
        print(f"'NPCs to Highlight' replaced by '%s'." % (npc_name))

    # Append new NPC name
    elif replace_or_append=='append':
        press_keys('ctrlleft', 'a', delay_after=0.5)
        press_keys('ctrlleft', 'c', delay_after=0.5)
        clipboard = pc.paste()
        npc_list = clipboard.lower().split(',')
        npc_exists = False
        for npc in npc_list:
            if npc==npc_name:
                npc_exists = True
        if npc_exists:
            print(f"'%s' already exists in 'NPCs to Highlight'." % (npc_name))
        else:
            press_keys('ctrlleft', 'end', delay_after=0.5)
            new_string = ""
            if clipboard[-1]!=',':
                new_string += ','
            new_string += npc_name
            type_string(phrase=new_string, delay_after=0.5)
            print(f"'%s' added to 'NPCs to Highlight'." % (npc_name))

    return 1