'''
a program to draw a circle and a square
'''

import turtle

t = turtle.Turtle()

def draw_circle(radius):
    t.circle(radius)

def draw_shape(sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

draw_circle(100)
draw_shape(4, 100)
