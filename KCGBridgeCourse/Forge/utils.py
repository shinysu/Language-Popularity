'''
utils module with two functions draw_shape and  move
'''
def draw_shape(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

def move(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
