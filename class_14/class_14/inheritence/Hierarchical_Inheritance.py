
class Vehicle:
    def vehicle_info(self):
        print("this is vehicle class  \n")

class Car(Vehicle):
    def car_info(self):
        print("this is car class")

class Truck(Vehicle):
    def truck_info(self):
        print("this is truck class ")

obj1 = Car()
obj1.car_info()
obj1.vehicle_info()


obj2 = Truck()
obj2.truck_info()
obj2.vehicle_info()