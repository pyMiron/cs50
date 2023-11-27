import turtle
turtle.speed(20)
l=0
color_val=['red','blue','green','yellow','purple','brown']
for i in range(200):
    turtle.right(15)

    turtle.right(60)
    turtle.fd(i * 1.5)
    turtle.color(color_val[l])
    l+=1
    if l==6:
        l=0
