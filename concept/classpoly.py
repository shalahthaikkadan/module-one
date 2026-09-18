class Parent:

    x = 10

    def parent_method(self):
        print("This is a parent")

    def detail(self):
        print("hello")


class Child(Parent):
    x=20

    def detail(self):
        print("hi")
    


obj = Parent()
obj1 = Child()
print(obj1.x)
obj1.detail()