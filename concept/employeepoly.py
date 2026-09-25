class FullTimeEmployee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee:

    def __init__(self, name, hour_rate, hours_worked):
        self.name = name
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked

class Freelancer:
    def __init__(self, name, project_rate,project): 
        self.name = name
        self.project_rate = project_rate
        self.project = project

    def calculate_salary(self):
        return self.project_rate* self.project


obj = FullTimeEmployee('shalah', 22000)

print(obj.name)
print(obj.calculate_salary())


obj1 = PartTimeEmployee('samil', 1000, 40)

print(obj1.name)
print(obj1.calculate_salary())

obj2 = Freelancer('sahal',10000,2)
print(obj.name)
print(obj2.calculate_salary())

#polymorphism
employees = [obj,obj1,obj2]
for employee in employees:
    print("name:", employee.name)
    print("salary:",employee.calculate_salary())
    
