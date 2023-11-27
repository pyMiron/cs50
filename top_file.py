import datetime

try:
    with open('text.txt','w')as file:
        file.write(f'today {datetime.date.today()}\n')
        file.write(f'now {datetime.datetime.now()}\n')
except:
    print('ошибка при работе с файлом')
