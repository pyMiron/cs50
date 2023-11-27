import pytesseract
import cv2
from PIL import Image
#img = Image.open('img.png')
#img = Image.open('eng.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = 'cheks1.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#custom_config = r'--oem 3 --psm 1'
#custom_config = r'--oem 3 --psm 2'
#custom_config = r'--oem 3 --psm 3'
#custom_config = r'--oem 3 --psm 4'
#custom_config = r'--oem 3 --psm 5'
#custom_config = r'--oem 3 --psm 6' best
#custom_config = r'--oem 3 --psm 6'
#custom_config = r'--oem 3 --psm 7'
#custom_config = r'--oem 3 --psm 8'
#custom_config = r'--oem 3 --psm 9'
#custom_config = r'--oem 3 --psm 10'
#custom_config = r'--oem 3 --psm 11' 2
#custom_config = r'--oem 3 --psm 12'
#custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(gray_image, config=custom_config, lang='eng' )
print(text)

