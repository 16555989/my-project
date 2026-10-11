import random

a = int(input("Введіть початок діапазону a: "))
b = int(input("Введіть кінець діапазону b: "))

masiv = [random.randint(a, b) for i in range(12)]

print("Початковий масив:", masiv)

masiv.sort()

print("Відсортований масив:", masiv)