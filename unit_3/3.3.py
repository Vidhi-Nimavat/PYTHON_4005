#3) Write a program to make use of class method and instance method.

class Student:

    def AddStudent(self,roll_no,name,age,gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender  = gender

    def DisplayStudent(self):
        print(f"Student roll_no is:{self.roll_no}")
        print(f"Student name is:{self.name}")
        print(f"Student age is:{self.age}")
        print(f"Student gender is:{self.gender}")

s1 = Student()
s1.AddStudent(1,"Vidhi",21,"female")
s1.DisplayStudent()
