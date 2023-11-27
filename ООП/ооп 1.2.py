# методы класса
class Point:
    color='red'
    circle=2

    def set_coords(self,x,y):
        #print('вызов set_coords'+str(self))
        self.x=x
        self.y=y
    def get_coords(self):
        return(self.x,self.y)
    #print(Point.set_coords)

pt=Point()
        #pt2=Point()
    #print(pt.set_coords)
pt.set_coords(1,2)
        #pt2.set_coords(10,20)
    #Point.set_coords(pt)
    #print(pt.__dict__)
        #print(pt2.__dict__)
print(pt.get_coords())
f=getattr(pt,'get_coords')
print(f())