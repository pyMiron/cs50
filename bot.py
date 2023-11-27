from datetime import datetime, time, date
vrema=datetime.today()
vr1=vrema.timetuple()
print('вас приветствует бот datetime, этот бот помогает узнавать дату, время и т.д. ')
print('список вопросов :')
print('какое сейчас время','какая сегодня дата',"какой сейчас год")
if vr1[1]==1:
    s='января'
elif vr1[1]==2:
    s='февраля'
elif vr1[1] == 3:
    s='марта'
elif vr1[1]==4:
    s='апреля'
elif vr1[1]==5:
    s='мая'
elif vr1[1]==6:
    s='июня'
elif vr1[1]==7:
    s='июля'
elif vr1[1]==8:
    s='августа'
elif vr1[1]==9:
    s='сентября'
elif vr1[1]==10:
    s='октября'
elif vr1[1]==11:
    s='ноября'
elif vr1[1]==12:
    s='декабря'


while True:
    a=input('введите ваш вопрос :')
    if a.lower()!='stop'and a.lower()!= 'стоп':
        print('если хотите закончить напишите стоп или stop')
    if a.lower()=='какое сейчас время':
        print(vr1[3],'часов',vr1[4],'минут',vr1[5],'секунд',sep=' ')
    elif a.lower()=='какая сегодня дата':
        print(vr1[2],s,sep=' ')
    elif a.lower()=="какой сейчас год":
        print(vr1[0])
    elif a.lower()=='стоп'or 'stop':
        break
    else:
        print('вы ввели что то не то ')


