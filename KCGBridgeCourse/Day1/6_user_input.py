'''
draw a polygon - get input from user
key concept - get user input using input() function
            - int() function to convert the user input to integer
'''

import turtle

def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

print("Enter the number of sides")
sides = int(input())
print("Enter the length of the sides")
length = int(input())
t = turtle.Turtle()
draw_shape(t, sides, length)
