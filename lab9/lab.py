N = int(input("Введіть кількість планет: "))

planets = ("Меркурій", "Венера", "Земля", "Марс",
           "Юпітер", "Сатурн", "Уран", "Нептун")

for i in range(min(N, len(planets))):
    print(planets[i])