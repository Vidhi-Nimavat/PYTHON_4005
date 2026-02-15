#WAP to print prime number series between 1 to 50

for num in range(2, 51):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num, end=" ")
