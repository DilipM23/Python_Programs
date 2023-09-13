import math

class Shape :
    def _init_(self):
        self.area = 0
        self.name = " "
    
    def displayArea(self):
        print("The area of", self.name, " is ",self.area)
    
class Circle(Shape):
    def __init__(self, radius):
        self.area = 0
        self.name = "Circle"
        self.radius = radius
    
    def calarea(self):
        self.area = math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self,length, breadth):
        self.area = 0
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth
    
    def calArea(self):
        self.area = self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.area = 0
        self.name = "Triangle"
        self.base = base
        self.height = height
    
    def calArea(self):
        self.area = self.base * self.height / 2

c = Circle(5)
c.calarea()
c.displayArea()

r = Rectangle(4,5)
r.calArea()
r.displayArea()

t = Triangle(4,5)
t.calArea()
t.displayArea()