import telebot

bot = telebot.TeleBot('6959679079:AAE_Ez1AZN4RcTl0xlS1EWPfxedk_m1GEbs')
photo = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('отправить фото', callback_data='photo'))
    bot.send_message(message.chat.id, f'привет {message.from_user.first_name} есть чем поделиться или есть вопросы? Присылайте фото сюда, опубликуем (с указанием ника или анонимно, по желанию).',reply_markup=markup)

    bot.register_next_step_handler(message, 'start1')


def start1(message):
    #if telebot.types== 'photo':
    bot.send_message(message.chat.id, 'присылайте свое фото')
    bot.register_next_step_handler(message, 'image_func')

@bot.message_handler(content_types=['photo'])
def image_func(message):
    global photo
    photo = message.photo[-1]
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('отправить фото', callback_data='photo'))
    bot.send_message(message.chat.id, 'ваше фото было успешно отправлено на усмотрение администрации', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    #bot.reply_to("1755845698", photo)
    if callback.data == 'photo':
        bot.reply_to(callback.message.chat.id, 'анонимно или с указанием ника')
        bot.send_message(callback.message.chat.id, 'ваше фото было успешно отправлено на усмотрение администрации')
bot.infinity_polling()
