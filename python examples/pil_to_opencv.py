# Tests convesion of image from PIL format to openCV format

import cv2
import PIL
from PIL import Image
import numpy as np
import os

file_name = os.path.basename(__file__)
print(f"Executing %s..." % file_name)
image_path = os.path.join(os.getcwd(), 'images', 'icons', 'runelite.png')
pil_image = PIL.Image.open(image_path).convert('RGB') 
open_cv_image = np.array(pil_image) 
open_cv_image = open_cv_image[:, :, ::-1].copy()
print("Displaying image...")
cv2.imshow("Test image", open_cv_image)
cv2.waitKey(0)
print(f"Completed %s." % file_name)