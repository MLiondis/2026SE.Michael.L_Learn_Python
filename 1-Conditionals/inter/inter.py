x, y, z = input("Calc: ").split(" ")
x = int(x)
z = int(z)

if y == "+":
    ans = x + z
elif y == "-":
    ans = x - z
elif y == "*":
    ans = x * z
elif y == "/":
    ans = x / z

print(f"{ans:.1f}")