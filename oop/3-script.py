#!/usr/bin/env python3

# Polymorphism:
# Create a Figure class with a calculate_area() method. Then, create derived classes
# like Circle and Rectangle that implement the method differently.

class Figure():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def calculate_area(self):
        # Method to calculate and return the area based on width and height
        return f'Calculating the area with a width of {self.width} and a height of {self.height}'


class Circle(Figure):
    def __init__(self, width, height, radius) -> None:
        super().__init__(width, height)
        self.radius = radius

    def calculate_area(self):
        # Override the base class method to include circle-specific area calculation
        return super().calculate_area() + f' and a radius of {self.radius}, so the area would be {(self.radius**2) * 3.1416} cm2'


class Rectangle(Figure):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)

    def calculate_area(self):
        # Override the base class method to include rectangle-specific area calculation
        return super().calculate_area() + f'. The area is {self.width * self.height}'


circle = Circle(10, 10, 5)
rectangle = Rectangle(10, 10)

# Test the overridden methods for Circle and Rectangle
print(circle.calculate_area())
# Calculating the area with a width of 10 and a height of 10 and a radius of 5

print(rectangle.calculate_area())
# Calculating the area with a width of 10 and a height of 10. The area is 100