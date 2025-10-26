def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))

print_table(n1)
print_table(n2)