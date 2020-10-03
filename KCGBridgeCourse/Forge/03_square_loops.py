'''
draw a square using loop
The statements within the for loop executes 4 times for i values, 0, 1, 2,3
key concept - using loops for repeated statements
'''

import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90)
