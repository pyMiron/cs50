import turtle


args = input()

turtle.begin_fill()
if args=='moon':
    turtle.color('blue')
    turtle.circle(50)
elif args=='sun':
    turtle.color('yellow')
    turtle.circle(75)
turtle.end_fill()