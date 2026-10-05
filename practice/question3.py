#3.Write a function area() that works differently for Square and Rectangle classes.
# Demonstrate method overriding for calculating area.

class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


obj1 = Square(5)
print("Area of square:", obj1.area())

obj2 = Rectangle(10, 3)
print("Area of rectangle:", obj2.area())