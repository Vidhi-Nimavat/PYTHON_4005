#Write a program to read a file which contains only numbers. Display total 
#of all numbers with maximum and minimum number.

file=open("numbers.txt","w")
file.write("10\n20\n30\n40\n50")
file.close()


file=open("numbers.txt","r")
content=file.read()
print(content)

data = list(map(int, content.split()))

print("Total of numbers:",sum(data))
print("Maximum of numbers:",max(data))
print("Minumum of numbers:",min(data))

file.close()
