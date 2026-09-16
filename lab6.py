import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a

for i in range(int((b - a) / h) + 1):
    y = abs(math.tan(abs(x) + 0.1))
    print("x =", x, "y =", y)
    x = x + h