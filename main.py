import telebot
import sqlite3
bot = telebot.TeleBot('6604263906:AAFUmHD-TusrdtVYizlrE1DHvVEn3wZluFU')
name = None


@bot.message_handler(commands=['set_homework'])
def set_homework(message):

    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS homework_list ( name text primary key, pass text)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'привет, сейчас запишем твою домашку, пиши предмет')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip().lower()
    bot.send_message(message.chat.id, 'введите само дз')
    bot.register_next_step_handler(message, user_home)


def user_home(message):
    homework = message.text.strip().lower()

    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute(
        'INSERT INTO homework_list (name, pass) VALUES ("%s", "%s")' % (name, homework))
    conn.commit()
    cur.close()
    conn.close()

    # main_dict[name] = homework
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список дз', callback_data='homework_list'))
    bot.send_message(message.chat.id, 'домашнее задание записано!', reply_markup=markup)


@bot.message_handler(commands=['update_homework'])
def update_homework(message):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS homework_list ( name text auto_increment primary key, pass text)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'привет, сейчас изменим твою домашку, пиши предмет')
    bot.register_next_step_handler(message, up_user_name)


def up_user_name(message):
    global name
    name = message.text.strip().lower()
    bot.send_message(message.chat.id, 'введите само дз')
    bot.register_next_step_handler(message, up_user_home)


def up_user_home(message):
    homework = message.text.strip().lower()
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute(f'UPDATE homework_list SET pass = "{homework}" WHERE name = "{name}"')

    conn.commit()
    cur.close()
    conn.close()

    # main_dict[name] = homework
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список дз', callback_data='homework_list'))
    bot.send_message(message.chat.id, 'домашнее задание записано!', reply_markup=markup)


@bot.message_handler(commands=['get_homework'])
def get_homework(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список дз', callback_data='homework_list'))
    bot.send_message(message.chat.id, 'вот ваше дз', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM homework_list')
    homework_list = cur.fetchall()

    info = ''
    for el in homework_list:
        info += f'предмет : {el[0]}, дз : {el[1]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

    print(info)


@bot.message_handler(commands=['del_homework'])
def del_homework(message):
    bot.send_message(message.chat.id, 'привет, сейчас удалим твою домашку, пиши предмет')
    bot.register_next_step_handler(message, del_user_name)

def del_user_name(message):
    global name
    name = message.text.strip().lower()
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute(f"DELETE FROM homework_list WHERE name = '{name}'")

    conn.commit()
    cur.close()
    conn.close()
bot.infinity_polling()
