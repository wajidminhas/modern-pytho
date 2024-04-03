

class Person():
    def __init__(self, name: str, sex: str, profession: str) -> None:
        # data members (instance variables)
        self.name: str = name
        self.sex: str = sex
        self.profession: str = profession

    # Behavior (instance methods)
    def show(self) -> None:
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self) -> None:
        print(self.name, 'working as a', self.profession)

    def warrior(self) -> None:
        print(f"{self.name} is a warrior and has been fought many wars.")

p1 : Person = Person("wajid", "male", "developer")
# print("Name:", p1.name, "Sex:", p1.sex, "Profession:", p1.profession)

class Address(Person):
    pass


p2 : Address = Address("sajid", "male", "developer")

print(p2.name)
p2.show()
p2.work()
p2.warrior()