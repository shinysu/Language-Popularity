'''
get random colour for the shape
use list to store a list of colors to chose from
'''

import turtle
from random import randint
from utils import draw_shape, move

t = turtle.Turtle()
def get_random_color():
    colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    shape_color = colours[randint(0, len(colours) - 1)]
    return shape_color

sides = randint(3, 8)
length = randint(50, 300)
move(t, 100, 100)
colour = get_random_color()
t.color(colour)
t.begin_fill()
draw_shape(t, sides, length)
t.end_fill()