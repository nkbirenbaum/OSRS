# Main script used to run sets of other functions

# Import libraries
from runelite import *
from functions import *
from gui import *


# Entry point
def main(): 

    # Start GUI
    check_os_version()
    create_gui()

    # focus_rl_window()
    # update_rl_window_position()
    # login_osrs()
    # standardize_view()

    # # Start combat training
    # highlight_npc('cow')



# Enter script at main
if __name__ == '__main__':
    main()

