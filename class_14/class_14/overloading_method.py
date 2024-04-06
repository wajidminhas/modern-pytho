from typing import Union, overload

# @overload
# def add(x: int, y : int)-> int:
#     ...

# @overload
# def add(x : float, y : float)->float:
#     ...

# @overload
# def add(x : str, y : str)-> str:
#     ...

def add(x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    elif isinstance(x, str) and isinstance(y, str):
        return x + y
    else:
        raise TypeError("Unsupported types for addition")

# Example usage:
print(add(5, 10))  # Output: 15
print(add(3.5, 2.5))  # Output: 6.0
# print(add(3.8, "hello"))
print(add('Hello ', 'world'))  # Output: Hello world