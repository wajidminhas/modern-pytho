
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle Class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Car Class")

car :Car = Car()

car.car_info()
car.vehicle_info()



