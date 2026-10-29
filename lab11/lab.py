
import csv
import math

a = float(input("Введіть початок діапазону: "))
b = float(input("Введіть кінець діапазону: "))
h = float(input("Введіть крок: "))

with open("func.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])

    x = a
    while x <= b + 1e-9:
        y = math.exp(x) + 0.1 * x ** 2
        writer.writerow([round(x, 4), round(y, 4)])
        x += h

print("Таблицю записано у файл func.csv")
