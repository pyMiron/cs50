class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

# работает с данными которые внутри класса типо переменных
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

# работает сама по себе с данными которые внутри метода
    @staticmethod
    def norm2(x, y):
        return x*x + y*y


V = Vector(1, 2)
print(Vector.validate(5))
res = V.get_coord()
print(res)
print(Vector.norm2(5, 6))
