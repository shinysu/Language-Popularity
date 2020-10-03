'''
get random colour for the shape
use list to store a list of colors to chose from
'''
import turtle
from random import randint

t = turtle.Turtle()

def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def get_random_color():
    colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    shape_color = colours[randint(0, len(colours) - 1)]
    return shape_color

sides = randint(3, 8)
length = randint(50, 300)
move(100, 100)
colour = get_random_color()
t.color(colour)
t.begin_fill()
draw_shape(t, sides, length)
t.end_fill()