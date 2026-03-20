#9) Write a program to do student operations using menu as follows
#a) Add Student
#b) Search Student
#c) List All Students
#d) Update Student
#e) Delete Student
#f) Exit

list=[]
while True:
    print("1.Add Student")
    print("2.Search Student")
    print("3.List All Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")

    choice=int(input("Enter your choice from 1 to 6..."))

    if choice==1:
        name=input("Enter name for append:")
        list.append(name)

    elif choice==2:
        search_stud=input("Enter name for search...")
        if search_stud in list:
            print("Student is in list")
            print(list)

        else:
            print("Student is not in list")
            print(list)

    elif choice==3:
        print("List of students:",list)

    elif choice==4:
        update=int(input("Enter which value you want to change. Enter value number:"))
        update_val=input("Enter updated value:")
        list[update]=update_val
        print(list)

    elif choice==5:
        delete_val=int(input("Enter which value you want to delete. Enter value number:"))
        del list[delete_val]
        print(list)

    elif choice==6:
        print("You are exit from program.")
        exit()

    else:
        print("Enter valid choice")
        
        
        
