#data=input()
#file = open('data/text.txt', 'w')
#file.write(data + "\n")
#file.close()

file=open("data/text.txt","r")
print(file.read())
for line in file:
    print(line,end="")
file.close()