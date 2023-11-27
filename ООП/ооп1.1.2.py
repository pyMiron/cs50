class Point:
    "класс для представление координат точек на плоскости"   #строка с описанием класса
    color='red'     #аттрибуты класса
    circle=2
a=Point()
b=Point()
a.x=1
setattr(a,'y',2)
setattr(b,'x',10)
b.y=20

print(Point.__doc__) #содержит строку с описанием класса
print(a.__dict__) #содержит набор аттрибутов класса
print(b.__dict__)

