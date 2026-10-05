#Create a base class Person with attributes name and age.
#Derive a class Employee that adds salary. 
#Show how to create an object of Employee and display all details.

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,salary):
          super().__init__(name,age)
          self.salary=salary

obj=Employee("shalah",22,22000)
print("Name:", obj.name)
print("age",obj.age)
print("salary",obj.salary)