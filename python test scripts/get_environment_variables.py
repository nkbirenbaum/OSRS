import os
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get('RUNELITE_WINDOW_X'))
print(os.environ.get('RUNELITE_WINDOW_Y'))