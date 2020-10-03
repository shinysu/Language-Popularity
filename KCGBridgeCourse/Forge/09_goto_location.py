'''
move the turtle to a location and draw the shape
t.goto(x, y) is used move the turtle to the location(x,y) in screen
'''
import turtle
from random import randint

t = turtle.Turtle()

def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

sides = randint(3, 8)
length = randint(50, 300)

t.penup()
t.goto(100, 100)
t.pendown()

t.color("green")
t.begin_fill()
draw_shape(t, sides, length)
t.end_fill()