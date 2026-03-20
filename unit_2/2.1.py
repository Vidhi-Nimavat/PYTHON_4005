#Write a program to display basic exception handling in python
try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    result=num1/num2
    print("Result is:",result)

except ZeroDivisionError:
        print("Can not devide by zero.")
except ValueError:
    print("Enter integer value for calculation for division.")

except Exception as e:
    print("Unexpected Error:",e)

else:
    print("Division successfull!")

finally:
    print("Program executed successfully (with or without error).")
