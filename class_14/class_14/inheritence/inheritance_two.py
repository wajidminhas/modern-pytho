class Person:
    country: str = "Pakistan"

    def __init__(self, name: str, cnic: int) -> None:
        self.name = name
        self.cnic = cnic

class Address(Person):
    def __init__(self, name: str, cnic: int, address: str) -> None:
        super().__init__(name, cnic)
        self.address = address

class Material(Person):
    def __init__(self, name: str, cnic: int, is_married: bool) -> None:
        super().__init__(name, cnic)
        self.marital_status = is_married

class BankAccount(Person):
    def __init__(self, name: str, cnic: int, bank_name: str) -> None:
        super().__init__(name, cnic)
        self.bank_name = bank_name

bank1 = BankAccount("bala", 1234, "SBI")
print(bank1.bank_name, bank1.cnic)

address1 : Address = Address("bala", 1234, "Karachi")
print(address1.address, address1.cnic, address1.name)
