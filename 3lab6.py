import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

spisok = []

x = a

while x <= b:
    y = abs(math.tan(abs(x) + 0.1))
    spisok.append([x, y])
    x += h

print("Список:")
print(spisok)

dobutky = []

for ryadok in spisok:
    dobutky.append(ryadok[0] * ryadok[1])

print("Добутки:")
print(dobutky)