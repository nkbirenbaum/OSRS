import tkinter as tk
import math
from functions import *
from runelite import *

# Creates GUI window
def create_gui():
    
    # Create window
    gui = tk.Tk()
    gui.title("OSRS bot GUI")
    gui_resize(gui, w=500, h=500)
    gui_reposition(gui, x=200, y=200)
    gui.resizable(0, 0)

    # Create frame
    frm_buttons = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # Place buttons in 2 columns on grid
    buttons = {}
    for ii, _ in range(8):
        buttons[ii] = tk.Button(master=frm_buttons, width=16)
        buttons[ii].grid(row=math.floor(ii/2), column=ii%2, sticky="e")

     # Add text and commands to buttons
    buttons[0].configure(text="Open RuneLite", command=lambda: open_rl())
    buttons[1].configure(text="Login", command=lambda: login_osrs())
    buttons[6].configure(text="Screenshot all", command=lambda: save_screen(area='all'))
    buttons[7].configure(text="Screenshot game", command=lambda: save_screen(area='game'))
    
    gui.mainloop()


# Resize the GUI window
def gui_resize(gui, w, h):

    size_str = str(w) + 'x' + str(h)
    gui.geometry(size_str)
    return 1


# Reposition the GUI window
def gui_reposition(gui, x, y):

    position_str = '+' + str(x) + '+' + str(y)
    gui.geometry(position_str)
    return 1