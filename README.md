## OSRS

Scripts & GUI to create a bot to play Old School Runescape. Work in progress.

# To do
- move_mouse_to() 
    - Implement mouse overshoots
- GUI
    - Add tkinter bindings to pause/exit
    - Make sure bindings can be used when window is out of focus


# Useful commands & notes
+ Update requirements: 
    + pip freeze > requirements.txt 
+ Install requirements: 
    + pip install -r requirements.txt 
+ Remove from GitHub after pushing: 
    + git rm --cached FILE_NAME 
+ Install pytesseract:
    + https://stackoverflow.com/questions/46140485/tesseract-installation-in-windows
+ Open subprocess
    + subprocess.run(EXE_PATH, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW)
