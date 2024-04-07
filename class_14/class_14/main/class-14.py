

class Mother:
    def __init__(self, name : str)->None:
        self.name : str = name
        self.eyecolor : str = "blue"

class Father:
    def __init__(self, name: str) -> None:
        self.name : str = name
        self.height : str = "5.9 feet"

class Child(Mother, Father):
    def __init__(self, mohter_name: str, father_name : str, child_name : str) -> None:
        Mother.__init__(self, mohter_name)
        Father.__init__(self, father_name)
        self.child_name : str = child_name

wajid : Child = Child("sajida perveen", "shabbir hussain", "wajid shabbir")

print(f"wajid height is {wajid.height}")
print(f"wajid's eye color is {wajid.eyecolor}")
