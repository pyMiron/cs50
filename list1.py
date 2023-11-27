n= int(input("enter len: "))
miron_list=[]
i=0

while i<n:
    kik = "element #" + str(i + 1) + ": "
    miron_list.append(input(kik))
    i+=1
print(miron_list)