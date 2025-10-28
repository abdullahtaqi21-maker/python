print("              1\n")
import math as m
value1 = input("Enter a number:")
value = float(value1)
print(f"You entered:{value}")

sqrt = m.sqrt(value)
print(f"The square root of {value} is {sqrt}")

print("\n              2")

exp = input("Enter the exponent:")
power = input("Enter the power:")
print(f"{exp} raised to the power {power} is {m.pow(float(exp), float(power))}")