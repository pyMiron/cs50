# паттерн моносостояния   элементы в первом обьекте класса равны элеменнтам во втором обьекте класса
class ThreadData:
    __shared_attrs = {
        'name': "thread1",
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


tr1 = ThreadData()
tr2 = ThreadData()
print(tr1.__dict__)
print(tr2.__dict__)
