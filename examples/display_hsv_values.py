import os
import cv2 
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


image_file = os.path.join(os.getcwd(), 'examples', 'images', 'yellow_box.png')
img_pil = Image.open(image_file)
img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_BGR2RGB)
print(img_cv)
cv2.imshow("Yellow bar", img_cv)
cv2.waitKey(0)

