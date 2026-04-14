'''10) Write a program to overload addition (+) and subtraction (-) (Use 
appropriate methods to overload the same.'''
class Number:
    def __init__(self, value):
        self.value = value

    # Overloading +
    def __add__(self, other):
        return Number(self.value + other.value)

    # Overloading -
    def __sub__(self, other):
        return Number(self.value - other.value)


# Main Program
n1 = Number(20)
n2 = Number(10)

add_result = n1 + n2     # calls __add__()
sub_result = n1 - n2     # calls __sub__()

print("Addition:", add_result.value)
print("Subtraction:", sub_result.value)
