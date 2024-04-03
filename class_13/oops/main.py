

class Person():
    def __init__(self, person_id, person_name) -> None:
        self.person_id : int = person_id
        self.person_name : str = person_name
    
    def address(self, add:str)->None:
        print(f"{self.person_name} belong to {add}")

obj1 : Person = Person(3421, "sir zia")
obj2 : Person = Person(536346, "sir qasim")

print(obj1.person_id, obj1.person_name)
print(obj2.person_id, obj2.person_name)


obj1.address("karachi")
obj2.address("lahore")

class Balaaj():
    def __init__(self, name, age) -> None:
        self.name : str = name
        self.age : int = age

    def __str__(self) -> str:
        return f"name : {self.name} \nage : {self.age}"
    def Marketing(self)->None:
        print(f"{self.name} is a marketing person")

    def Finance(self)->None:
        print(f"{self.name} is a finance person")

obj3 : Balaaj = Balaaj("sir zia", 34)
print(obj3)
obj3.Marketing()
obj3.Finance()