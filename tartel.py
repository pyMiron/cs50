import turtle
from turtle import *
turtle.reset()
screen = turtle.Screen()
screen.bgcolor("blue")
# звезда
#turtle.speed(5)
def star(x,y):
    turtle.fillcolor('yellow')
    turtle.pencolor('yellow')
    turtle.setposition(x,y)
    begin_fill()
    turtle.lt(60)
    turtle.fd(25)
    turtle.rt(120)
    turtle.fd(25)
    turtle.rt(145)
    turtle.fd(30)
    turtle.rt(155)
    turtle.fd(30)
    turtle.rt(155)
    turtle.fd(30)
    end_fill()
def home(x,y):
    goto(x,y)

    # for background
    screen = turtle.Screen()
    screen.bgcolor("blue")




    turtle.fillcolor('cyan')
    turtle.begin_fill()
    turtle.rt(90)
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(400)
    turtle.lt(90)
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(400)
    turtle.rt(90)
    turtle.end_fill()

    # for top of
    # the house
    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.rt(45)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(200)
    turtle.lt(180)
    turtle.fd(200)
    turtle.rt(135)
    turtle.fd(259)
    turtle.rt(90)
    turtle.fd(142)
    turtle.end_fill()

    # for door and
    # windows
    turtle.rt(90)
    turtle.fd(400)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(180)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(75)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(180)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(75)
    turtle.lt(90)
    turtle.fd(15)
    turtle.lt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(15)
    turtle.rt(90)
    turtle.fd(75)

home(-10,-30)
star(-40,100)
