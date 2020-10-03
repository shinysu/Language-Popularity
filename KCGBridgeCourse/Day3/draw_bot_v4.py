'''
use else condition to handle all other cases
lower() - convert a string to lower case
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

polygon_sides = {'triangle': 3, 'square': 4, 'pentagon': 5, 'hexagon': 6, 'septagon': 7, 'octagon': 8}

print("What would you like to draw?")
user_input = input().lower()
if user_input == 'circle':
    draw_circle(100)
elif user_input in polygon_sides:
    draw_shape(polygon_sides[user_input], 100)
else:
    print("Sorry, can't draw that shape")

print("Thank You!")