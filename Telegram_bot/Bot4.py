import telebot
import requests
import  json
bot = telebot.TeleBot('6664414561:AAFXjSmlE8lyFuEYHGSJRljeiMnd-Zctjt4')
API = '7e97e8cbd20b7135578bb2f5779c1570'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]['temp']
        weather = data['weather'][0]['main']
        if weather == 'Rain':
            weat = 'дождь'
        elif weather == 'Clear':
            weat = 'ясно'
        elif weather == 'Clouds':
            weat = 'облачно'
        elif weather == 'Mist':
            weat = 'туман'
        else:
            weat = weather

        bot.reply_to(message, f'сейчас температура в {city} : {temp}, погода {weat}')
    else:
        bot.reply_to(message, 'город указан неверно')


bot.polling(none_stop=True)