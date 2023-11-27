class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name=name
        self.age=age
        self.isHappy=isHappy
    def get_data(self):
        print(self.name,"age:",self.age,". Happy",self.isHappy)

cat1= Cat()
cat1.set_data('sheridan',13,True)

cat2=Cat()
cat2.name="gosha"
cat2.age= 7
cat2.isHappy= False

print(cat1.name)
print(cat2.name)
cat1.get_data()
cat2.get_data()

