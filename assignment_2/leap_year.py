#WAP to check whether a given year is a leap year.

year=int(input("Enter year for check whether it is leap year or not:"))

if year%4==0:
    print(year, "this is leap year.")

else:
    print(year, "this is not leap year.")
