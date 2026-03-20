'''11.Write a program to create function which shall accept any number of 
arguments and display total of all the numbers given as argument.'''

def calculate_total(*args):
    total = 0
    for num in args:
        total+=num
    print("Total=",total)

calculate_total(10,20,30,40,50)


    
