import os
from dotenv import set_key

dotenv_path = os.getcwd() + "\.env"
# set_key(dotenv_path, 'RUNELITE_WINDOW_X', str(123))
# set_key(dotenv_path, 'RUNELITE_WINDOW_Y', str(789))
set_key(dotenv_path, 'FLAG_DEBUG_MOUSE_POSITION', str(1))
set_key(dotenv_path, 'FLAG_DEBUG_MOUSE_CLICK', str(1))
