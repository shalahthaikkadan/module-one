
def addition(x,y):
   return x+y

def sub(x,y):
   return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    try:
          return x//y
    except ZeroDivisionError:
        print("Division by zero not allowed")
    finally:
        print("execution completed")




      
          
  
      