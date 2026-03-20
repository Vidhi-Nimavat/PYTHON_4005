#4) Write a program to make use of inner class

class Student:

    def stuentDetails(self):
        self.no=int(input("Enter your no:"))
        self.name=input("Enter your name:")

    def display(self):
        print(f"No is:{self.no}")
        print(f"Name is:{self.name}")

    class marks:

        def marksDetail(self):
            self.m1=float(input("Enter your Python marks:"))
            self.m2=float(input("Enter your Network marks:"))
            self.m3=float(input("Enter your Android marks:"))

        def displayMarks(self):
            print(f"Python marks:{self.m1}")
            print(f"Network marks:{self.m2}")
            print(f"Android marks:{self.m3}")

    c2=marks()
    c2.marksDetail()
    c2.displayMarks()

c1=Student()
c1.stuentDetails()
c1.display()
        
