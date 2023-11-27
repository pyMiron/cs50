class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    # автоматически вызывается при получении свойства класса с именем item

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)
    # автоматически вызывается при изменении свойства key класса

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('недопустимое имя аттрибута')
        else:
            object.__setattr__(self, key, value)
            # self.__dict__[key] = value
        # автоматически вызывается при получении несуществующего свойства item класса

    def __getattr__(self, item):
        # print('__getattr__' + item)
        return False
        # автоматически вызывается при удалении свойства item (не важно есть оно или нет)

    def __delattr__(self, item):
        print('__delattr__' + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x
print(pt1.__dict__)


'''a = pt1.y
print(pt1.__dict__)
print(Point.__dict__)'''
