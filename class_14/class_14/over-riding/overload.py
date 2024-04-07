from typing import overload, Union

class Adder:
    @overload
    def add(self, x: int, y: int) -> int:
        ...
        
    @overload
    def add(self, x: float, y: float) -> float:
        ...
        
    @overload
    def add(self, x: str, y: str) -> str:
        ...
       

    def add(self, x : Union[int, str, float], y : Union[int, str, float]) -> Union[int, str, float]:
        if isinstance(x , int) and isinstance(y , int):
            return x + y
        elif isinstance(x , str) and isinstance(y , str):
            return x + y
        elif isinstance(x , float) and isinstance (y , float):
            return x + y
        else :
            raise TypeError("invalid argument types")

    
        
        

# Create an instance of the class
addition_num = Adder()

# Call the overloaded methods
result1 = (addition_num.add(1, 2))
result2 = (addition_num.add("wajid ", "shabbir"))
result3 = (addition_num.add(59.9,45.8))

print(f"Interger Addition : {result1}" )
print(f"string addition : {result2}" )
print(f"float addition :  {result3}")
