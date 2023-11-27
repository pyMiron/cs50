class Point:
    color='red'
    circle=2
    def __init__(self,x=0,y=0):  #инициализатор объекта ,вызывается сразу после создания объекта класса
        #print('вызов __init__')
        self.x=x
        self.y=y

    def __del__(self):  #финализатор объекта ,вызывается перед удалением объекта класса
        print('удаление экземпляра'+str(self))

    def set_coords(self,x,y):
        self.x=x
        self.y=y

    def get_coords(self):
        return(self.x,self.y)

pt= Point(1,2)

print(pt.__dict__)