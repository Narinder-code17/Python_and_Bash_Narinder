# Write to a File

file = open("output.txt", "w")

file.write("Hello, this is my Python file handling assignment.\n")
file.write("Python can create and write data into text files.\n")
file.write("This file was created using open() and write().\n")

file.close()

print("Content written to output.txt successfully.")