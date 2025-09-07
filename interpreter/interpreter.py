expresion = input("Math Expression ")

x, y, z = expresion.split(" ")
x = int(x)
z = int(z)

if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")
else:
    print("wrong expresion")