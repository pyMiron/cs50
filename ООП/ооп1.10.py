from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзиклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('фио должна быть строкой')

        f=fio.split()
        if len(f) != 3:
            raise TypeError('неверный формат ФИО')

        letters = ascii_letters +cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('в фио должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('в ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int:
            raise TypeError('возраст должен быть числом')
        if 14 > old > 120:
            raise TypeError('возраст должен быть в диапазоне от 14 до 120')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) not in (int, float):
            raise TypeError('вес должен быть числом')
        if 20 > weight:
            raise TypeError('вес должен быть не меньше 20 килограмм')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('паспорт должен быть строкой')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) !=6:
            raise TypeError('неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError("серия и номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__ps

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__ps = ps


p = Person('Романов Мирон Вячеславович', 30, '1234 567890', 88.0)
p.old = 100
p.passport = '9345 234958'
p.weight = 66.0
print(p.__dict__)