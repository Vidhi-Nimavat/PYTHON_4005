#Write a program to read file which has marks entry of student and display 
#details with total, percentage and grade (Consider a file which has 
#comma separated data with RollNo, Student Name, Mark1, Mark2, Mark3 
#and Mark4)
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

with open("marks.txt.txt", "r") as file:
    for line in file:

        line = line.strip()

        # Skip empty or invalid lines
        if not line or "," not in line:
            continue

        data = line.split(",")

        if len(data) != 6:
            print("Skipping invalid line:", line)
            continue

        rollno = data[0]
        name = data[1]

        marks = list(map(int, data[2:]))

        total = sum(marks)
        percentage = total / 4
        grade = calculate_grade(percentage)

        print("\n--- Student Details ---")
        print("Roll No   :", rollno)
        print("Name      :", name)
        print("Total     :", total)
        print("Percentage:", percentage)
        print("Grade     :", grade)
