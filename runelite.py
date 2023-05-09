import os
import pyperclip as pc
from dotenv import load_dotenv
from functions import move_mouse
from functions import click_mouse
from functions import press_keys
from functions import press_key
from functions import type_string
from functions import action_delay


# Opens RuneLite configuration sidebar
def open_rl_configuration():

    # Check whether configuration is already open
    # TO DO

    # Click small configuration button
    move_mouse(x_end=785, y_end=40, x_tol=10, y_tol=10, delay_after=0.5)
    click_mouse(delay_after=0.5)

    # Click large configuration button
    move_mouse(x_end=810, y_end=50, x_tol=10, y_tol=10, delay_after=0.5)
    click_mouse(delay_after=0.5)

    print("RuneLite configuration opened.")
    return 1


# Open plugin settings
def open_rl_plugin_settings(plugin_name=''):

    # Return if plugin_name is empty
    if plugin_name=='':
        print(f"Error in open_rl_plugin_settings(): plugin_name argument cannot be empty.")
        return 0

    # Load window position
    load_dotenv()
    runelite_window_x = int(os.environ.get('RUNELITE_WINDOW_X'))
    runelite_window_y = int(os.environ.get('RUNELITE_WINDOW_y'))

    # Select search bar
    x_end = runelite_window_x + 870
    y_end = runelite_window_y + 98
    move_mouse(x_end, y_end, x_tol=50, y_tol=5)
    action_delay(0.500, 0.200)
    click_mouse()

    # Type plugin name
    action_delay(0.500, 0.200)
    type_string(plugin_name)
    action_delay(0.500, 0.200)

    # Click plugins settings
    x_end = runelite_window_x + 962
    y_end = runelite_window_y + 137
    move_mouse(x_end, y_end, x_tol=5, y_tol=5)
    action_delay(0.500, 0.200)
    click_mouse()
    action_delay(0.500, 0.200)

    return 1


# Highlight NPC
def highlight_npc(npc_name='', append_or_replace='replace'):

    # Return if npc_name is empty
    if npc_name=='':
        print(f"Error in highlight_npc(): npc_name argument cannot be empty.")
        return 0
    npc_name = npc_name.lower()

    # Return if append_or_replace is not 'append' or 'replace'
    append_or_replace = append_or_replace.lower()
    if append_or_replace=='append' or append_or_replace=='replace':
        print(f"Error in highlight_npc(): unrecognized input '%s' for 'append_or_replace' argument." % (append_or_replace))
        return 0

    # Open RuneLite configuration sidebar & NPC Indicators settings
    open_rl_configuration()
    open_rl_plugin_settings('npc indicators')

    # Load window position
    load_dotenv()
    runelite_window_x = int(os.environ.get('RUNELITE_WINDOW_X'))
    runelite_window_y = int(os.environ.get('RUNELITE_WINDOW_y'))

    # Enter NPCs to highlight text box
    x_end = runelite_window_x + 880
    y_end = runelite_window_y + 475
    move_mouse(x_end, y_end, x_tol=5, y_tol=5)
    action_delay(0.500, 0.200)
    click_mouse()
    action_delay(0.500, 0.200)

    # Replace with new NPC name
    if append_or_replace=='replace':
        press_keys('ctrlleft', 'a')
        action_delay(0.500, 0.200)
        press_key('delete')
        action_delay(0.500, 0.200)
        type_string(npc_name)
        print(f"NPC Indicators replaced by %s" % (npc_name))

    # Append new NPC name
    elif append_or_replace=='append':
        press_keys('ctrlleft', 'a')
        action_delay(0.500, 0.200)
        press_keys('ctrlleft', 'c')
        action_delay(0.500, 0.200)
        clipboard = pc.paste()
        npc_list = clipboard.lower().split(',')
        npc_exists = False
        for npc in npc_list:
            if npc==npc_name:
                npc_exists = True
        if npc_exists:
            print(f"%s already exists in NPC Indicators" % (npc_name))
        else:
            press_keys('ctrlleft', 'end')
            action_delay(0.500, 0.200)
            new_string = ""
            if clipboard[-1]!=',':
                new_string += ','
            new_string += npc_name
            new_string += ','
            print(f"%s added to NPC Indicators" % (npc_name))

    return 1