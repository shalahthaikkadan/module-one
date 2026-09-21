class Student:
    count=0

    def __init__(self,name):
        self.name=name
        Student.count += 1

    def detail(self):
        print(f'my name is {self.name}')

    #class method
    @classmethod
    def class_method(cls):
        print(f'Student count:{cls.count}')
        
    #instance method
    @staticmethod
    def static_method(a,b):
        return a+b

obj=Student('shalah')
obj.detail()
Student.class_method()
print(Student.static_method(1,2))