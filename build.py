class Building:
    year=None
    city=None

    def __init__(self,year,city):
        self.year=year
        self.city=city

    def get_info(self):
        print('year:',self.year,"city:",self.city)


class school(Building):
    pupils=0

    def __init__(self,pupils,year,city):
        super(school,self).__init__(year,city)
        self.pupils=pupils

class house(Building):
    pass



class shop(Building):
    pass


school = school(100,2000,"Moskow")
school.get_info()
houes= Building(2000,'Moskow')
shop= Building(2000,"Moskow")
