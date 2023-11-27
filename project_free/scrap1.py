import telebot
import sqlite3
import snscrape
bot =telebot.TeleBot('6672739538:AAHGwO160P_NAHnfWTwnkt9bp9DPrDWjAXY')

def collect_posts(channel):
    with open(f'{channel}.txt') as file:
        file = file.readlines()
    posts = []



bot.polling(none_stop=True)