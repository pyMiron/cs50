#x=[4,56,7.8,9,0,-3,'robot',False,[7,9,10]]
#print(x)
#x[2]=8
#print(x)
#print(x[-1])
#print(x[-1][1])
#x[:] дублирует список
num=[9,2,7] #список
num.append(3) #добавление одного элемента
num.insert(1,True) #присваивание индексу элемент с последующим перемещением элементов списка
num.extend([5,6,4]) #добавление нескольких элементов
num.sort() #сортировка списка
num.reverse() #переворачивает список
num.pop(-2) #извлечение последнего элемента списка,или извлечение элемента по индексу
num.remove(True)  #удаление первого элемента списка по его названию
# num.clear() #очищает список
# print(num.count(3)) #ищет сколько элементов с таким значением есть в списке
print(len(num)) #длина списка
print(num)