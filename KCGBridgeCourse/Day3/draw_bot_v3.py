'''
using dictionary to store the number of sides for the polygon type
dictionary store data as key-value pair. Here the name of the polygon is the key and the number of sides is stored as the value
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
user_input = input()
if user_input == 'circle':
    draw_circle(100)
elif user_input in polygon_sides:
    sides = polygon_sides[user_input]
    draw_shape(sides, 100)

print("Thank You!")
