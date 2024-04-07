

class Person():
    def person_info(self, name, age):
        print("Inside Person class")
        print(f"Name : {name}, Age :  {age}\n")

class Company():
    def company_info(self, company_name : str, location : str):
        print("Inside Company Class")
        print(f"Company Name :  {company_name}, Location :  {location}\n" )

class Employee(Person, Company):
    def employee_info(self, salary : int, skill : str):
        print("Inside Employee Class")
        print(f"Salary : {salary}, Skill : {skill} ")

emp : Employee = Employee()

emp.person_info("wajid", 35)
emp.company_info("Balaaj enterprise", "Jhelum")
emp.employee_info(5000, "Devops")
