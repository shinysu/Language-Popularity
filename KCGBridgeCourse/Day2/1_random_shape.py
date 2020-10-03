'''
random shape - draw random shapes with random length
use  the randint() function to get a random integer in a range
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

t.color("green")
t.begin_fill()
draw_shape(t, sides, length)
t.end_fill()