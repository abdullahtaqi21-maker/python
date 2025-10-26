def greet():
    print("Hello, welcome to FLA")
greet()

def greet2(n):
    print(f"Hello, {n}! Welcome to FLA")

greet2("Taqi")
greet2("Ali")


def greet3(n = "Guest"):
    print(f"Hello, {n}! Welcome to FLA")

greet3()
greet3("Fatima")