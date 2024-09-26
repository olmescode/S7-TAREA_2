import math

class Calculator:
    def __init__(self):
        # We could initialize attributes here if necessary
        pass

    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class AreaCalculator:
    def __init__(self):
        # We could initialize attributes here if necessary
        pass

    def square_area(self, side: float) -> float:
        return side ** 2
    
    def rectangle_area(self, length: float, width: float) -> float:
        return length * width
    
    def triangle_area(self, base: float, height: float) -> float:
        return (base * height) / 2
    
    def circle_area(self, radius: float) -> float:
        return math.pi * (radius ** 2)

# Usage example
if __name__ == "__main__":
    calc = Calculator()
    areas = AreaCalculator()

    print(f"Sum: {calc.add(5, 3)}")
    print(f"Square area: {areas.square_area(4)}")
    print(f"Circle area: {areas.circle_area(3)}")
