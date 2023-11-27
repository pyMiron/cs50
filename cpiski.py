country={"code":"RU","name":"Russia","population":144}
#country= dict(code="RU",name="Russia",population=144)
#print(country["code"])

#for key, value in country.items():
   # print(key,"-",value,sep="")
#print(country.get("name"))
#country.clear() очищает слоарь
#country.pop("name") извлечение из словаря
#country.popitem() извлечение последнего элемента
#print(country) пишет список
#print(country.values()) пишет значения
#print(country.keys()) пишет ключи
#print(country.items()) пишет и то и то

#country['code']='none'

#print(country)




person={
    "user_1":{
        "first_name": "Miron",
        "last_name": "romanov",
        "age": 16,
        "address": ("togliatty","70years of october st.",58),
    },
    "user_2":{

    }
}
print(person["user_1"]["address"][1])