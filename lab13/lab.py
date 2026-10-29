
class RIVER:
    def __init__(self, name, continent, length):
        self.name = name
        self.continent = continent
        self.length = length

    def change_name(self, name):
        self.name = name

    def change_length(self, length):
        self.length = length

    def display(self):
        print("Назва:", self.name)
        print("Континент:", self.continent)
        print("Довжина:", self.length, "км")


rivers = []

n = int(input("Кількість річок: "))

for i in range(n):
    name = input("Назва річки: ")
    continent = input("Континент: ")
    length = float(input("Довжина (км): "))

    rivers.append(RIVER(name, continent, length))

print("Список річок:")
for river in rivers:
    river.display()

if rivers:
    rivers[0].change_name(input("Нова назва першої річки: "))
    rivers[0].change_length(
        float(input("Нова довжина першої річки: "))
    )

    print("Після змін:")
    rivers[0].display()
