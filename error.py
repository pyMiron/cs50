#try:
 #   x = int(input('enter number'))
 #   x += 5
 #   print(x)
#except ValueError:
    #print("введите лучше число")
'''x=0
while x==0:
    try:
        x = int(input('enter number'))
        x += 5
        print(x)
    except ValueError:
        print("введите лучше число")
'''
try:
    x=5/0
except ZeroDivisionError: #отследживает ошибки
    print('деление на ноль')
except ValueError:
    print('вы ввели что то не то')
else:
    print('else')
finally:
    print("Finally")