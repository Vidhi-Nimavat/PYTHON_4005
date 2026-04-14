'''7) Use appropriate functions for each classWrite a program to display MRO using 
multiple inheritance. Multiple inheritance can be done as per your choice'''
# Parent Class 1
class A:
    def show(self):
        print("This is class A")

# Parent Class 2
class B:
    def show(self):
        print("This is class B")

# Child class inheriting from both A and B
class C(A, B):
    def display(self):
        print("This is class C")

# Main Program
obj = C()

# Calling methods
obj.display()
obj.show()   # Which show() will be called? Based on MRO.

# Displaying MRO
print("\nMethod Resolution Order:")
for cls in C.__mro__:
    print(cls)
