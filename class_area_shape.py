from abc import ABC, abstractmethod
class Shape():
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi*(self.radius**2)
    def perimeter(self):
        import math
        return math.pi*2*self.radius

radius = int(input("Enter the radius of circle = "))
circle1 = Circle(radius)

length = int(input("Enter the length of the rectangle = "))
width = int(input("Enter the width of the rectangle = "))
rectangle1 = Rectangle(length,width)

print(f"For rectangle with \nwidth {width} \nlength {length} \n area = {rectangle1.area()} \nperimeter = {rectangle1.perimeter()}")
print(f"For the circle with \nRadius = {circle1.radius} \n area = {circle1.area()} \n perimeter = {circle1.perimeter()}")

