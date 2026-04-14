'''9) Write a program to create interface and utilize the same in other class.'''
from abc import ABC, abstractmethod

# Interface (Abstract Class with only abstract methods)
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Class implementing the interface
class Car(Vehicle):

    def start(self):
        print("Car has started.")

    def stop(self):
        print("Car has stopped.")


# Main Program
obj = Car()
obj.start()
obj.stop()
