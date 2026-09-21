#a decorator is essentialy a function that takes another function as an arugument and return  anew function enhanced functionality.


def my_decorator(func):
    def wrapper():
        func()
        print("This is a decorator function")
    return wrapper

@my_decorator
def greet():
    pass

greet()