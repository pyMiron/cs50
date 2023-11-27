import pytesseract
import cv2
from PIL import Image

img = Image.open('cheks2.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split('.')[0]

my_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, lang='eng', config=my_config)
print(text)