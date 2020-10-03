'''
draw a square - replace all magic numbers with variables
key concept - using variables for storing values
'''

import turtle

t = turtle.Turtle()

sides = 4
length = 100
angle = 360 / sides

for i in range(sides):
    t.forward(length)
    t.left(angle)
