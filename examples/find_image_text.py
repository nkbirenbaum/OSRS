import os
import cv2 
import pytesseract

image_path = os.path.join(os.getcwd(), 'images', 'icons', 'runelite.png')
img = cv2.imread(image_path)

# Adding custom options - see https://nanonets.com/blog/ocr-with-tesseract/
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)