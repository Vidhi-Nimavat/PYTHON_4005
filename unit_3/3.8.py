'''8) Write a program to create abstract class with one method.'''
from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass   # Abstract method (must be overridden)


# Derived Class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Main Program
obj = Square(5)
print("Area of Square:", obj.area())
