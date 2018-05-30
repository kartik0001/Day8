# Q1.

import math

class circle():
    '''Class to get the Area of Circle and Circumference of a Circle'''
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return math.pi * (self.radius ** 2)

    def getCircumference(self):
        return 2 * math.pi * self.radius


radius = int(input("Enter the radius of Circle: "))
obj = circle(radius)
print("Area of the Circle:",(obj.getarea()))
print("Circumference of the Circle:",(obj.getCircumference()))



'''
OUTPUT:
Enter the radius of Circle: 5
Area of the Circle: 78.53981633974483
Circumference of the Circle: 31.41592653589793
'''