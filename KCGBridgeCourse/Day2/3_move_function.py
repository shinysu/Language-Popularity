'''
write a function to move the turtle
'''
import turtle
from random import randint

t = turtle.Turtle()

def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

sides = randint(3, 8)
length = randint(50, 300)
move(100, 100)
t.color("green")
t.begin_fill()
draw_shape(t, sides, length)
t.end_fill()