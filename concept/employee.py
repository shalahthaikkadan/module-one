class Employee:

    company_name = "TechNova Solutions"

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


class Developer(Employee):

    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print("Programming Language:", self.programming_language)


class Manager(Employee):

    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print("Team Size:", self.team_size)


developer = Developer("Shalah", 101, 50000, "Python")

manager = Manager("samil", 102, 70000, 10)


print("Developer Details")
developer.display_details()

print("Manager Details")
manager.display_details()


Employee.change_company_name("Zyvion Technologies")


print("After Changing Company Name")

print("Developer Details")
developer.display_details()

print("Manager Details")
manager.display_details()