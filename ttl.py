import turtle
color_val=['red','blue','pink','yellow']
for i in range(4):
    turtle.goto(0,0)
    turtle.color(color_val[i])
    turtle.right(90)
    for l in range(9):
        turtle.circle(l*10)

