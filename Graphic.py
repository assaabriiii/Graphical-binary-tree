from math import acos
from turtle import Turtle, Screen

DOT_DIAMETER = 20
GENERATION_DISTANCE = 75

def tree(turtle, d, origin):
    # d is the depth

    turtle.penup()
    turtle.setposition(origin)
    turtle.dot(DOT_DIAMETER)

    if d == 0:  # base case
        return

    distance = (GENERATION_DISTANCE**2 + (2**d * DOT_DIAMETER / 2)**2)**0.5
    angle = acos(GENERATION_DISTANCE / distance)

    turtle.pendown()
    turtle.left(angle)
    turtle.forward(distance)
    upper = turtle.position()
    turtle.right(angle)

    turtle.penup()
    turtle.setposition(origin)
    turtle.pendown()
    turtle.right(angle)
    turtle.forward(distance)
    lower = turtle.position()
    turtle.left(angle)

    tree(turtle, d - 1, upper)  # recurse upper branch
    tree(turtle, d - 1, lower)  # recurse lower branch

screen = Screen()

yertle = Turtle()
yertle.radians()  # to accommodate acos()

tree(yertle, 3, (-150, 0))

screen.mainloop()