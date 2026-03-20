#Write a program to copy a text file using file handling mechanism.

read_file=open("numbers.txt","r")

write_file=open("write.txt","w")

content=read_file.read()

write_file.write(content)
write_file.close()

content2=open("write.txt","r")
content3=content2.read()
print(content3)

read_file.close()
write_file.close()
content2.close()
