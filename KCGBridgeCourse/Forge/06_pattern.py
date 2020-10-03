'''
draw a pattern
'''

import turtle

def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

t=turtle.Turtle()
t.color("red")
for i in range(20):
    draw_shape(t, 4, 100)
    t.left(18)
