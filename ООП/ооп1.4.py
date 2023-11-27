class Point:
    def __new__(cls, *args, **kwargs):   #вызывается перед созданием обьекта класса
        print('вызов __new__ для'+str(cls))
        return super().__new__(cls)

    def __init__(self,x=0,y=0): #вызыватся сразу после создания обьекта класса
        print('вызов __init__ для'+str(self))
        self.x=x
        self.y=y

pt=Point(1,2)
print(pt)
