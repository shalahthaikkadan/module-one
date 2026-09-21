from abc import ABC,abstractmethod

class vechicle(ABC):

    @abstractmethod
    def start(self):
        pass

class car(vechicle):
    def start(self):
        print("The car is started with a key")

class bike(vechicle):
    def start(self):
        print("The bike is started with a key")

v1=car()
v1.start()

v2=bike()
v2.start()