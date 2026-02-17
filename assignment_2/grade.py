#WAP to display grade of a student based on percentage using if else ledder.

per=float(input("Enter your percentage to find grade:"))

if per>=90 and per<=100:
    print("Your grade is:A+")

elif per>=70 and per<=80:
    print("Your grade is:A")

elif per>=50 and per<=60:
    print("Your grade is:B")

elif per>=40 and per<50:
    print("Your grade is:C")

else:
    print("You are fail...")
