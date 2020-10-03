'''
draw a polygon - using a function
key concept - using functions for block of code that performs an action
    syntax: def function_name():
'''

import turtle

def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

t = turtle.Turtle()
draw_shape(t, 4, 100)
