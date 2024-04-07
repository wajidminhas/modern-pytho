

class Vehicle:
    def __init__(self, max_speed, mileage) -> None:
        self.max_speed : int = max_speed
        self.mileage : int = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)


# Create a Vehicle class without any variables and methods 

class Vehicle1:
    pass

#  Exercise 3: Create a child class Bus that will inherit all 
#  of the variables and methods of the Vehicle class

class Vehicle2:
    def __init__(self, name, max_speed, mileage) -> None:
        self.name : str = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle2):
    def __init__(self, name, max_speed, mileage) -> None:
        super().__init__(name, max_speed, mileage)
