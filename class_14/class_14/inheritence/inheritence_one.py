

class Employee():
    def __init__(self, name : str) -> None:
        print("Inside Employee class")
        self.name : str = name
        self.education : str = ""
        self.department : str = ""

class Designer(Employee):
    def __init__(self, title : str, name : str) -> None:
        super().__init__(name)
        # print("Inside Designer class")
        self.title : str = title

class Developer(Employee):
    def __init__(self, name: str, title : str) -> None:
        super().__init__(name)
        self.skill : list[str] = ["python"]

designer1 : Designer = Designer("Animation artist", "wajid shabbir")
developer1 : Developer = Developer("sajid", "backend developer")

print(designer1.title)
print(designer1.name)
print (developer1.name, developer1.skill)

