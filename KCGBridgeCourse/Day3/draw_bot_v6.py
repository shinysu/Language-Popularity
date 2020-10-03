'''
Get user input for length of the shape
int(input()) - used to convert user input to integer
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

while True:
    print("What would you like to draw?")
    user_input = input().lower()
    t.clear()
    if user_input == 'circle':
        radius = int(input("Enter the radius:"))
        draw_circle(radius)
    elif user_input in polygon_sides:
        length = int(input("Enter the length:"))
        draw_shape(polygon_sides[user_input], length)
    elif user_input == 'exit':
        print("Thank You!")
        exit(0)
    else:
        print("Sorry, can't draw that shape")
