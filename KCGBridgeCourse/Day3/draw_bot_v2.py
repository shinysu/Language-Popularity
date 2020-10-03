'''
using multiple elif statements for conditional check
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

print("What would you like to draw?")
user_input = input()
if user_input == 'circle':
    draw_circle(100)
elif user_input == 'square':
    draw_shape(4, 100)
elif user_input == 'pentagon':
    draw_shape(5, 100)
elif user_input == 'hexagon':
    draw_shape(6, 100)
elif user_input == 'septagon':
    draw_shape(7, 100)
elif user_input == 'octagon':
    draw_shape(8, 100)

print("Thank You!")