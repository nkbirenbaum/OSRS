import pyautogui as pag
import time
import winsound

frequency = 2000
duration = 300

# Acquire coordinates
print("Getting coordinates in 3 seconds...")
time.sleep(3)
x1, y1 = pag.position()
winsound.Beep(frequency, duration)
time.sleep(2)
x2, y2 = pag.position()
winsound.Beep(frequency, duration)
time.sleep(2)
x3, y3 = pag.position()
winsound.Beep(frequency, duration)
time.sleep(2)
x4, y4 = pag.position()
winsound.Beep(frequency, duration)
winsound.Beep(frequency+500, duration)
print("Coordinate acquisition complete.")

# Print coordinates
print("Coordinates:")
print("X1: ", x1, "\t\tY1: ", y1)
print("X2: ", x2, "\t\tY2: ", y2)
print("X3: ", x3, "\t\tY3: ", y3)
print("X4: ", x4, "\t\tY4: ", y4)

# Print metrics
