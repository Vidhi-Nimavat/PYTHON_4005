#WAP to implement the following operations on following list:
#list1=['physics','chemistry',1997,2000]
#list2=[1,2,3,4,5,6,7]

list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5,6,7]

concate=list1+list2
print("1.List Concatenation:")
print(concate)


print("2.Remove list1[3]")
del list1[3]
print(list1)


print("3.Add java in list1")
list1.append('java')
print(list1)

print("4.Update list2 as list2[3]=11")
list2[3]=11
print(list2)
