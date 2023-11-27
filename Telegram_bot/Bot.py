import telebot
import webbrowser
bot = telebot.TeleBot('6604263906:AAFUmHD-TusrdtVYizlrE1DHvVEn3wZluFU')


@bot.message_handler()
def site(message):
    webbrowser.open('https://www.youtube.com/watch?v=4xDzrJKXOOY')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'и тебе привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id{message.from_user.id}')


bot.polling(none_stop=True)

# bot.infinity_polling()
