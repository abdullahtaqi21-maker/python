file = open("data.txt", "r")
i = 1
for line in file:
    print(f"{i}.{line.strip()}")
    i += 1
file.close()