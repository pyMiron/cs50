import telebot
import pytesseract
import cv2
from PIL import Image
from telebot import types

bot = telebot.TeleBot('6664414561:AAFXjSmlE8lyFuEYHGSJRljeiMnd-Zctjt4')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 3 --psm 6'
image = None


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет я бот для считывания текста с картинки, пришли картинку')
    bot.register_next_step_handler(message, give_photo)


@bot.message_handler(content_types=['photo'])
def give_photo(message):
    global image
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'photo_bot.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, 'введите язык в формате (rus, eng)')
    bot.register_next_step_handler(message, give_lang)


def give_lang(message):
    lang = message.text.lower()
    text = pytesseract.image_to_string('photo_bot.jpg', config=custom_config, lang=lang)
    bot.send_message(message.chat.id, f'{text}')
bot.polling(none_stop=True)
