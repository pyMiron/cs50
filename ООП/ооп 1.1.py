#наследование
#инкапсуляция
#полиморфизм: параметрический

class Point:
    color='red'     #аттрибуты класса
    circle=2
Point.color='black'
print(Point.circle)
a=Point()
b=Point()
print(type(a))
print(isinstance(a,Point))
print(a.__dict__)
a.color='green'
print(a.color)
print(a.__dict__)
Point.type_pt = "disk"
setattr(Point,'prop',1)    #setattr добавление аттрибутов
setattr(Point,'type_pt','square')
res=Point.circle
print(res)
print(getattr(Point,'a',False)) #getattr возвращение аттрибута с возвращением false при его отсутствии
print(getattr(Point,'color'))
del Point.prop    #del удаление аттрибута из пространства имен
print(hasattr(Point,'prop')) #hasattr проверка на наличие аттрибута в пространстве имен
delattr(Point,'type_pt')   #delattr удаление аттрибута из пространства имен
print(hasattr(a,'circle'))
print(Point.__dict__)
