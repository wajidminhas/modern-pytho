
class Employee():
    def __init__(self, name) -> None:
        self.name : str = name
        self.education : str = "MCS"
        self.department : str = "IT"

class Designer(Employee):
    def __init__(self, name,  title : str) -> None:
        super().__init__(name)
        print("Inside calss Designer")
        self.title : str = title
      

class Developer(Employee):
    def __init__(self, name: str, title : str) -> None:
        super().__init__(name)
        self.title : str = title
        self.skill : list[str] = ["python"]

designer1 : Designer = Designer("wajid", "develper")
developer1 : Developer = Developer("sajid", "devops")
print(designer1.title, designer1.name)
print(developer1.name, developer1.skill, developer1.department, developer1.education)