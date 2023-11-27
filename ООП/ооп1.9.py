class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old
        print('удаление обьекта old')

        #property позволяет использовать геттеры и сеттеры удобнее

    #old = property(get_old, set_old)
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name
        print('удаление обьекта name')

    #name = property(get_name, set_name)


p = Person('Сергей', 20)

#p.__dict__['old'] = 'old in object p'

p.old = 35
#del p.old
p.name = 'Evgeniy'
print(p.old, p.name, p.__dict__)