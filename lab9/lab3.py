triangles = {}

n = int(input("Кількість трикутників: "))

for i in range(n):
    name = input("Назва трикутника: ")
    a, b, c = map(float, input("Введіть три сторони через пробіл: ").split())

    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        triangles[name] = S
    else:
        print("Трикутник не існує!")

if triangles:
    largest = max(triangles, key=triangles.get)
    print("Найбільша площа у трикутника:", largest)
    print("Площа:", round(triangles[largest], 2))
else:
    print("Немає правильних трикутників.")