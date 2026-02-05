import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

shapes = [
    Rectangle(10, 5),
    Circle(7),
    Rectangle(3, 3)
]

print("--- ООП підхід ---")
for shape in shapes:
    print(f"Площа фігури ({type(shape).__name__}): {shape.area():.2f}")