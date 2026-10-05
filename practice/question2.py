#Implement a class hierarchy:Vehicle (base) with method start_engine().
# Car (derived) with additional method play_music().
# ElectricCar (derived from Car) with method charge_battery().
# Demonstrate creating objects and calling all relevant methods.

class Vechicle():

    def start_engine(self):
        print("vechicle started")

class Car(Vechicle):
    def play_music(self):
        print("music is playing")

class ElectricCar(Car):
    def charge_battery(self):
        print("car is charging")



obj3= ElectricCar()
obj3.start_engine()
obj3.play_music()
obj3.charge_battery()






