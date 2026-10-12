s1 = input("Введіть перший рядок: ")
s2 = input("Введіть другий рядок: ")

for s in s1:
    if s in s2:
        print(s, end="")