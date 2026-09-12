# Read from a File

file = open("output.txt", "r")

content = file.read()

print("Content of output.txt:")
print(content)

file.close()