import sys
import os
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from runelite import focus_rl_window
from runelite import highlight_npc

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
focus_rl_window()
highlight_npc(npc_name='cow', replace_or_append='append')
print(f"Completed %s." % file_name)