import abdutils

name = input("Enter your name:")
n = abdutils.greet(name)

x = int(input("Enter a number:"))
sq = abdutils.square(x)
print(f"Square of {x} is {sq}")