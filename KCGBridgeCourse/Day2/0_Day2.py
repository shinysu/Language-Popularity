'''
fill the polygon with colors
'''
import turtle

t = turtle.Turtle()

def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

t.color("green")
t.begin_fill()
draw_shape(t, 4, 100)
t.end_fill()