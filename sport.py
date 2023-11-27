

sport={
    "chest":{
        "push-ups": ("narrow","wide","middle","on bars","negative"),
        "bench press": ("narrow","wide","middle"),
        "pullovers": "classic",
        "wiring": ("dumbbell ","crossovers"),
    },
    "back":{
        "pull-ups": ("narrow","wide","middle","negative"),
        "pulls": ("dumbdell","King's Pull","Deadlift","Тяга в наклоне"),
    },
    "Legs": ("squats","Barbell Squats","Lifting socks")

}
#print(sport["chest"]["push-ups"][2])
exercise=input("enter your muskles : ")
if exercise=="chest":
    print(sport["chest"])
elif exercise=="back":
    print(sport["back"])
elif exercise=="legs":
    print(sport["Legs"])
else:
    print("empty")
