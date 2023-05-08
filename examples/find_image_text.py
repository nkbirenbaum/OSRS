import os
import cv2 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

image_path = os.path.join(os.getcwd(), 'images', 'icons', 'runelite.png')
img = cv2.imread(image_path)

# Adding custom options - see https://nanonets.com/blog/ocr-with-tesseract/
custom_config = r'--oem 3 --psm 7'
print(pytesseract.image_to_string(img, config=custom_config))