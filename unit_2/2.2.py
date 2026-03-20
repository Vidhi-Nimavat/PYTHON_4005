#Write a program to execute user defined exception in python.

class MyError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        raise MyError("Negative number is not allowed")
    
    print("You entered:", num)

except MyError as e:
    print("Error:", e)
    
