'''2) Write a program to create a class for student with RollNo, Name, Age, 
Gender and methods named AddStudent() and DisplayStudent()
'''

class Student:

    def AddStudent(self):
        self.roll_no = int(input("Enter Your roll no:"))
        self.name = input("Enter name:")
        self.age = int(input("Enter age:"))
        self.gender  = input("Enter gender:")

    def DisplayStudent(self):
        print("Student Roll_no is:",self.roll_no)
        print("Student name is:",self.name)
        print("Student age is:",self.age)
        print("Student gender is:",self.gender)

s1 = Student()
s1.AddStudent()
s1.DisplayStudent()
