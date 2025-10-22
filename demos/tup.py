marks = (50, 70, 80)
# immutable (cannot be changed)
print(marks)

print(marks[0])
print(marks[-1])

numbers = (10,20,30,40,50)
print(numbers[1:4])

colors = ("red", "green", "blue")
colorList = list(colors)
colorList[1] = "yellow"
colors = tuple(colorList)
print(colors)  # ('red', 'yellow', 'blue')

t1 = (10, 20, 30)
t2 = (80,90)
t3 = t1 + t2
print(t3)

print(t1 * 100)