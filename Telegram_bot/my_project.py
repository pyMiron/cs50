import telebot
import sqlite3
bot = telebot.TeleBot('6604263906:AAFUmHD-TusrdtVYizlrE1DHvVEn3wZluFU')
name = None
group = ''
@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id, f'привет {message.from_user.first_name} напиши из какой ты группы(гум,хб)')
    bot.register_next_step_handler(message, start_1)
def start_1(message):
    global group
    group = message.text.strip().lower()
    if group not in ['гум', 'хб']:
        bot.send_message(message.chat.id, 'неверно указано имя группы, попробуй еще раз(гум, хб)')
        bot.register_next_step_handler(message, start)
   # bot.register_next_step_handler(message, teaming)
    else:

#def teaming(message):
        bot.send_message(message.chat.id, 'отлично мы записали тебя в базу данных')
        conn = sqlite3.connect('../11v.sql')
        cur = conn.cursor()

        cur.execute(
            'CREATE TABLE IF NOT EXISTS groups ( id int auto_increment primary key, name text)')
        cur.execute(
            'INSERT INTO groups (id, name) VALUES ("%s", "%s")' % (message.from_user.id, group))
        conn.commit()
        cur.close()
        conn.close()


@bot.message_handler(commands=['set_homework'])
def set_homework(message):
    key = message.from_user.id

    conn = sqlite3.connect('../11v.sql')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM groups WHERE id = "{key}"')
    result = cur.fetchone()
    #if result == 'гум':
    cur.execute(
        'CREATE TABLE IF NOT EXISTS homework_list_gum ( name text auto_increment primary key, pass text)')
    #elif result == 'хб':
    cur.execute(
        'CREATE TABLE IF NOT EXISTS homework_list_hb ( name text auto_increment primary key, pass text)')
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

    conn = sqlite3.connect('../11v.sql')
    cur = conn.cursor()
    key = message.from_user.id
    cur.execute(f'SELECT * FROM groups WHERE id = "{key}"')
    result = cur.fetchone()
    print(result)
    if result[1] == 'гум':
        cur.execute(
            'INSERT INTO homework_list_gum (name, pass) VALUES ("%s", "%s")' % (name, homework))
    if result[1] == 'хб':
        cur.execute(
            'INSERT INTO homework_list_hb (name, pass) VALUES ("%s", "%s")' % (name, homework))
    conn.commit()
    cur.close()
    conn.close()

    # main_dict[name] = homework
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список дз', callback_data='homework_list'))
    bot.send_message(message.chat.id, 'домашнее задание записано!', reply_markup=markup)


@bot.message_handler(commands=['update_homework'])
def update_homework(message):
    conn = sqlite3.connect('../11v.sql')
    cur = conn.cursor()
    key = message.from_user.id
    cur.execute(f'SELECT * FROM groups WHERE id = "{key}"')
    result = cur.fetchone()
    #if result == "гум":
    cur.execute(
        'CREATE TABLE IF NOT EXISTS homework_list_gum ( name text auto_increment primary key, pass text)')
    #elif result == 'хб':
    cur.execute(
        'CREATE TABLE IF NOT EXISTS homework_list_hb ( name text auto_increment primary key, pass text)')
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
    conn = sqlite3.connect('../11v.sql')
    cur = conn.cursor()
    key = message.from_user.id
    cur.execute(f'SELECT * FROM groups WHERE id = "{key}"')
    result = cur.fetchone()
    if result[1] == 'гум':
        cur.execute(f'UPDATE homework_list_gum SET pass = "{homework}" WHERE name = "{name}"')
    elif result[1] == 'хб':
        cur.execute(f'UPDATE homework_list_hb SET pass = "{homework}" WHERE name = "{name}"')
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
    conn = sqlite3.connect('../11v.sql')
    cur = conn.cursor()
    key = call.from_user.id
    cur.execute(f'SELECT * FROM groups WHERE id = "{key}"')
    result = cur.fetchone()
    info1 = ''
    info2 = ''
    if result[1] == 'гум':
        cur.execute('SELECT * FROM homework_list_gum')
        homework_list1 = cur.fetchall()

        for el1 in homework_list1:
            info1 += f'предмет : {el1[0]}, дз : {el1[1]}\n'

    elif result[1] == 'хб':
        cur.execute('SELECT * FROM homework_list_hb')
        homework_list2 = cur.fetchall()


        for el2 in homework_list2:
            info2 += f'предмет : {el2[0]}, дз : {el2[1]}\n'
    if result[1] == 'гум':
        bot.send_message(call.message.chat.id, 'гумы: ' + info1)
    elif result[1] == 'хб':
        bot.send_message(call.message.chat.id, 'химбио:' + info2)

    cur.close()
    conn.close()


    print(info1, info2)


@bot.message_handler(commands=['del_homework'])
def del_homework(message):
    bot.send_message(message.chat.id, 'привет, сейчас удалим твою домашку, пиши предмет')
    bot.register_next_step_handler(message, del_user_name)

def del_user_name(message):
    global name
    name = message.text.strip().lower()
    conn = sqlite3.connect('../11v.sql')
    cur = conn.cursor()
    key = message.from_user.id
    cur.execute(f'SELECT * FROM groups WHERE id = "{key}"')
    result = cur.fetchone()
    if result[1] == 'гум':
        cur.execute(f"DELETE FROM homework_list_gum WHERE name = '{name}'")
    elif result[1] == 'хб':
        cur.execute(f"DELETE FROM homework_list_hb WHERE name = '{name}'")
    conn.commit()
    cur.close()
    conn.close()
bot.infinity_polling()
