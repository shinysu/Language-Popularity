'''
draw_bot_v1.py
- uses input() function to get the user input
- use if, elif to check for a condition and perform an action
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

print("Thank You!")