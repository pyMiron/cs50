import telebot
import sqlite3

bot = telebot.TeleBot('6604263906:AAFUmHD-TusrdtVYizlrE1DHvVEn3wZluFU')
name = None

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), group varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'привет, сейчас тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'введите вашу группу (гумы, хим-био)')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass, id) VALUES ("%s", "%s","%s")' % (name, password, str(message.from_user.id)))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'имя :{el[1]}, пароль:{el[2]},id:{el[0]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

#raise sqlite3.IntegrityError('пользователь с таким id уже зарегистрирован')

bot.polling(none_stop=True)