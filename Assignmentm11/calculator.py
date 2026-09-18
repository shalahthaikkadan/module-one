x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
opr=input("Enter the operator: ")

def addition(x,y):
    result=x+y
    print(result)

def subtraction(x,y):
    result=x-y
    print(result)

def multiplication(x,y):
    result=x*y
    print(result)

def division(x,y):
    result=x/y
    print(result)

if opr=="+":
    addition(x,y)

elif opr=="-":
    subtraction(x,y)

elif opr=="*":
    multiplication(x,y)
    
elif opr=="/":
    division(x,y)  
      