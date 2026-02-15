#WAP 1*1 + 2*2 + 3*3......n*n

val=int(input("Enter number for get total of square of number:"))
sum=0

for i in range(1,val+1):
    sq=i*i
    print(sq)
    sum=sum+sq
print("Total of square:",sum)
