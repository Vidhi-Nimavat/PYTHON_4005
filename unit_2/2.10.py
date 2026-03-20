#Write a program to zip and unzip particular files.

import zipfile
# Create a ZipFile and add file into it
with zipfile.ZipFile('my_zip_file.zip', 'w') as zip_file:
    # Add a file to the zip file
    zip_file.write('error.txt')
print("Fize zipped successfully")

# Close the ZipFile object
zip_file.close()

with zipfile.ZipFile('my_zip_file.zip', 'r') as zip_file:
    # Extract all the files from the zip file
    zip_file.extractall()   # Files will be appear in current directory
# if we use  : zip_file.extractall(‘output_folder’) then files will be appear in current_folder                                 
print("Files extracted successfully")
# Close the ZipFile object
zip_file.close()   
