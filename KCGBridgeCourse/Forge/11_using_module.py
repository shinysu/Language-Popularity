'''
move the draw_shape() and move() functions to a module names utils.py and import it here
'''
import turtle
from random import randint
from utils import draw_shape, move

t = turtle.Turtle()
sides = randint(3,8)
length = randint(50,300)

move(t, 100, 100)
t.color("red")
draw_shape(t, sides, 100)
move(t, -100,-100)
draw_shape(t, sides, 100)
