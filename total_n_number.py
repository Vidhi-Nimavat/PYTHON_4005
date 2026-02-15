#total of n natural numbers

num=int(input("Enter number for find total value of square of each number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i

print("Sum of n natural numbers is:",sum)
