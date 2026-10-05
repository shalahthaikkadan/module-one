#Create a base class Shape with a method draw(). Derive classes Circle, 
# Rectangle, and Triangle that override draw(). 
class Shape:

    def draw(self):
        print("Drawing")

class Circle(Shape):

    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):

    def draw(self):
        print("Drawing a rectangle")

class Triangle(Shape):

    def draw(self):
        print("Drawing a triangle")


obj1=Circle()
obj1.draw()

obj2=Rectangle()
obj2.draw()

obj3=Triangle()
obj3.draw()