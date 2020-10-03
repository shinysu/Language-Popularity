'''
There are three types of triangles based on the sides.
An equilateral triangle is one in which all the sides are equal
An isosceles triangle has two equal sides
A scalene triangle has all sides of different length
Write a program that can get the three sides of a triangle and determine if the triangle is equilateral or isosceles or scalene
'''

x = int(input())
y = int(input())
z = int(input())

if x == y and x == z:
    print("Equilateral triangle")
elif x == y or y == z or x == z:
    print("Isosceles triangle")
else:
    print("Scalene triangle")