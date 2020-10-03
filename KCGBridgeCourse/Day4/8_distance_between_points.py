'''
program that determines the distance between two given points
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
print("Distance=", distance)