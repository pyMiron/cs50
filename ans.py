import datetime
def answers():
    print('список вопросов:')
    print('какая на улице погода,','какое сейчас время,','кто написал эту программу,','как зовут президента Российской федерации,','в каком году распался советский союз')
    answer=''
    print('введите стоп если хотите закончить')
    while answer!='стоп':
        answer=input('введите вопрос:')
        if answer=='какая на улице погода':
            print('хорошая погода')
        elif answer=='какое сейчас время':
            print(datetime.datetime.now())
        elif answer=='кто написал эту программу':
            print('начинающий разработчик на питоне')
        elif answer=='как зовут президента Российской федерации':
            print('Владимир Владимирович Путин')
        elif answer=='в каком году распался советский союз':
            print('в 1991')


