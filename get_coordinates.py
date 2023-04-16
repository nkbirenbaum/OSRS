import pyautogui as pag
import time
import winsound
import numpy as np
from functions import countdown

frequency = 2000
duration = 300

# Initialize arrays
x = np.empty(1, 4)
y = np.empty(1, 4)

# Acquire coordinates
print("Getting coordinates in 3 seconds...")
countdown()
time.sleep(0.5)
n = 4
for ii in range(n):
    x[ii], y[ii] = pag.position()
    if ii == n-1:
        winsound.Beep(frequency+500, duration)
    else:
        winsound.Beep(frequency, duration)
        time.sleep(2)

# Calculate metrics
x_max = np.max(x)
y_max = np.max(y)
x_min = np.min(x)
y_min = np.min(y)

# Print coordinates & metrics
print("Coordinates:")
for ii in range(n):
    print("Point ", ii, ": (", x[ii], ", ", y[ii], ")")
print("Max: (", x_max, ", ", y_max, ")")
print("Min: (", x_min, ", ", y_min, ")")
