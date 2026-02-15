#1.WAP for print the fabonacci series.

a=0
b=1
val=int(input("Enter how many value you want to print in fibonacci series:"))
print(a,b,sep="\n")

for i in range(3,val+1):
    c=a+b
    a=b
    b=c
    print(c)
