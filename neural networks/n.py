import pytesseract
from PIL import Image

#img = Image.open('img.png')
img = Image.open('eng.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split('.')[0]

#custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='eng', config=custom_config)
print(text)

with open('phone_number.txt', 'w') as text_file:
    text_file.write(text)