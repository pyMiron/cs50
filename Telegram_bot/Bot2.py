import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('6604263906:AAFUmHD-TusrdtVYizlrE1DHvVEn3wZluFU')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('перейти на музыку')
    markup.row(btn1)
    btn2 = types.KeyboardButton('удалить фото')
    btn3 = types.KeyboardButton('изменить текст')
    markup.row(btn2, btn3)
    file = open('../neural networks/img.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_audio(message.chat.id, file, reply_markup=markup)
    #bot.send_video(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, 'привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'перейти на музыку':
        webbrowser.open('https://www.youtube.com/watch?v=4xDzrJKXOOY')
    elif message.text == 'удалить фото':
        bot.delete_message(message.chat.id, message.message_id - 1)
    #bot.register_next_step_handler(message, on_click)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('перейти на музыку', url='https://www.youtube.com/watch?v=4xDzrJKXOOY')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'какое красивое фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.infinity_polling()
