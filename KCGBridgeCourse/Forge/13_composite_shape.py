'''
draw a house
'''
import turtle
from random import randint
from utils import draw_shape, move

t = turtle.Turtle()

def get_random_color():
    colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    shape_color = colours[randint(0, len(colours) - 1)]
    return shape_color

colour = get_random_color()
t.color(colour)
t.begin_fill()
draw_shape(t, 4, 100)
t.end_fill()

'''triangle roof of the house'''
move(t, 0, 100)
colour = get_random_color()
t.color(colour)
t.begin_fill()
draw_shape(t, 3, 100)
t.end_fill()

'''door of the house'''
move(t, 40, 0)
colour = get_random_color()
t.color(colour)
t.begin_fill()
draw_shape(t, 4, 20)
t.end_fill()
