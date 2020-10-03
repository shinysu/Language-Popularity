'''
get the radius of the circle and calculate the area of the the circle
round() - used to round of a number to two decimal points
'''

from math import pi

def find_area(radius):
    area = pi * radius * radius
    return area


input_radius = int(input("Enter radius: "))
area = find_area(input_radius)
print("Area of circle: ", round(area, 2))