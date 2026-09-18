x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
opr=input("Enter the operator: ")

class Calculator:

    def addition(self, x, y):
        return x+y

    def subtraction(self, x, y):
        return x-y

    def multiplication(self, x, y):
        return x*y

    def division(self, x, y):
        try:
            result = x // y
            print(result)
        except ZeroDivisionError:
            print("Division by zero not allowed")
        finally:
            print("Execution completed")
    



obj = Calculator()

if opr=="+":
   print(obj.addition(x,y))
if opr=="-":
   print(obj.subtraction(x,y))
if opr=="*":
   print(obj.multiplication(x,y))
if opr=="/":
   print(obj.division(x,y))
