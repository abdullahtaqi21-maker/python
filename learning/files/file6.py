file = open("notes.txt", "r+")
print(file.read())
file.write("\nPython!")
file.close()