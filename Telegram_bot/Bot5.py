import telebot
from currency_converter import CurrencyConverter
from telebot import types
bot = telebot.TeleBot('6664414561:AAFXjSmlE8lyFuEYHGSJRljeiMnd-Zctjt4')
Currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, введите сумму')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
        bot.register_next_step_handler(message, summa)
        return
    if amount <=0:
        bot.send_message(message.chat.id, 'Число должно быть положительным. Впишите сумму')
        bot.register_next_step_handler(message, summa)
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
    btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
    btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
    btn4 = types.InlineKeyboardButton('другое значение', callback_data='else')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'выберите пару валют', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = Currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'получается: {round(res,2)}. Можете заново вписать сумму')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'введите пару значений через /')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = Currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'получается: {round(res, 2)}. Можете заново вписать сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'что то не так попробуйте еще раз')
        bot.register_next_step_handler(message, my_currency)
bot.polling(none_stop=True)