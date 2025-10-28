import abdutils

print("-" * 25)

name = input("Enter your name:")
n = abdutils.greet(name)

print("-" * 25)

x = int(input("Enter a number:"))
sq = abdutils.square(x)
print(f"Square of {x} is {sq}")

print("-" * 25)

n2 = int(input("Enter a number:"))
n1 = abdutils.print_table(n2)

print("-" * 25)