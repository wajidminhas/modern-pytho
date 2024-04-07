

class MathOperation:
    @staticmethod
    def add(a : int,  b : int)-> int:
        return a + b
    
    @staticmethod
    def multiply(a : int,  b : int)-> int:
        return a * b
    
result_add = MathOperation.add(10, 20)
result_multiply = MathOperation.multiply(10, 20)

print("addition : ", result_add )
print("multiplication : ", result_multiply)