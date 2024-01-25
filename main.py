from __future__ import annotations
class Point:
    def __init__(self, x:int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def  __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self,another_point: Point) -> str:
        result_x = self.x + another_point.x
        result_y = self.y + another_point.y
        return f"({result_x}, {result_y})"
    
    def __sub__(self, another_point: Point) -> Point:
        result_x = self.x - another_point.x
        result_y = self.y - another_point.y
        return Point(result_x, result_y)
    
    def __eq__(self, another_point:Point) -> bool:
        return self.x == another_point.x and self.y == another_point.y
    
# p1 = Point(5,0)
# p2= Point(10,15)
# p3 = p1 - p2
# print(p3)
# print(p1 == p2)


class ComplexNumber:
    def __init__(self, real: int, img: int) -> None:
        self.real = real 
        self.img = img
    
    def __add__(self, cx: ComplexNumber) -> ComplexNumber:
        result1 = self.real + cx.real
        result2 = self.img + cx.img
        return ComplexNumber(result1, result2)
    
    def __sub__(self, cx: ComplexNumber) -> ComplexNumber:
        result1 = self.real - cx.real
        result2 = self.img - cx.img
        return ComplexNumber(result1, result2)
    
    def  __repr__(self) -> str:
        return f"({self.real} {str(self.img)[0] if self.img < 0 else '+'} {self.img}j)"

    
a = ComplexNumber(5, 5)
a2 = ComplexNumber (1, 2)
a3 = a + a2
print(a3)