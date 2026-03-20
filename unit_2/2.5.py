#Write a program to read a file and display its contents. At the end it shall also display no. of
#words available in file.

file=open("2.1.py","r")

content=file.read()

print(content)

words=content.split()

word_count=len(words)

print("Number of words in file:",word_count)

file.close()
