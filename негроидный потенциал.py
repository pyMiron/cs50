import random
d=0
e=0
s=[1,2,3,4,5,6,7,8,9]
a=input("введите имя-")
random.shuffle(s)
while True:
    print("приветствую мирон!  приветствую",a,"!")
    print("начнем игру")
    while e<3 or d<3:
        f=s.pop()
        hodd=int(input())
        hoda=int(input("ваш ход мирон"))
    if hodd==f and hoda==f:
        d+=1
        e+=1
        print('вы оба были правы')
        break
    elif hodd==f:
        d+=1
        print("игрок",a,'получает одно очко количество очков=',d)
        break
    elif hoda==f:
        e+=1
        print("игрок мирон получает одно очко количество очков=",e)
        break
    else:
        print("никто не получает очко")
        break
if e==3:
    print("победитель мирон!!!")
elif d==3:
    print("победитель",a)
