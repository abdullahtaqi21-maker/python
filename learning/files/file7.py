
filename = "notes.txt"

note = input("Enter your note: ")

f = open(filename, "a")

f.write("\n" + note)

f.close()

print("Note saved successfully!")
