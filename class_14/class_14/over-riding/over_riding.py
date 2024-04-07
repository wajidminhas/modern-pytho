
# over riding
class Animal:
    def eating(self, food: str) -> None:
        print(f"Animal eats {food}")

class Bird(Animal):  # Inherit from Animal class
    def eating(self, food: str) -> None:
        print(f"Bird eats {food}")

# animal = Animal()
# animal.eating("grass")

bird : Bird = Bird()
bird.eating("grain")

# POLY-MARPHISM

animal : Animal = Bird()
animal.eating('grass')

# here we can check the type of animal class
print(type(animal))