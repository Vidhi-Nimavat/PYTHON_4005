'''10.Write a program to create 4 lambda functions which shall accept 2 
numbers and one arithmetic operator. As per arithmetic operator related 
lambda functions shall be invoked.'''

x=int(input("Enter number1:"))
y=int(input("Enter number2:"))
op=input("Enter operator for arithmetic operation from this:+,-,*,/:")

if op=="+":
    addition = lambda x, y: x + y
    print("Addition is:",addition(x,y))

elif op=="-":
    subtract = lambda x, y: x - y
    print("Subtrcation is:",subtraction(x,y))

elif op=="*":
    multiply = lambda x, y: x * y
    print("Multiplication is:",multiply(x,y))

elif op=="/":
    divide = lambda x, y: x / y
    print("Division is:",divide(x,y))

else:
    print("Give valid operator...")
