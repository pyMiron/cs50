import random

stroka=input()
str_lst=list(stroka)
random.shuffle(str_lst)
stroka=str_lst

str_stroka=''.join(stroka)
print(str_stroka)
