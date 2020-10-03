'''
Two circles touch each other if the distance between the centers of the circle is less than the sum of the radii of both
circles.
Write a program that gets the position of the center of the circles and the radius and determines if the circles
touch each other.
'''

from math import sqrt

def find_distance(x1, y1, x2, y2):
    distance_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    distance = sqrt(distance_sq)
    return distance


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
distance = find_distance(x1, y1, x2, y2)
r1 = int(input("Radius1: "))
r2 = int(input("Radius2: "))

if distance == r1 + r2:
    print("Circles touch ech other")
elif distance > r1 + r2:
    print("Circles do not touch each other")
else:
    print("Circles overlap")
