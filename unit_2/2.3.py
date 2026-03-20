#Write a program to generate arithmetic exception and log the exception in system.
import logging
logging.basicConfig(filename="error.txt", level=logging.ERROR)

try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    result=num1/num2
    print("Result is:",result)

except Exception as e:
    print("Can not devide by zero.")
    logging.error(e)
    

