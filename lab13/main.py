
from enterprise import ENTERPRISE

enterprises = []

n = int(input("Кількість підприємств: "))

for i in range(n):
    name = input("Назва підприємства: ")
    finance = float(input("Активи (тис. грн): "))
    year = int(input("Рік створення: "))
    owner = input("Власник: ")

    enterprises.append(
        ENTERPRISE(name, finance, year, owner)
    )

print("Підприємства з активами понад 1 млн грн:")
for enterprise in enterprises:
    if enterprise.GetFinance() > 1000:
        enterprise.DisplayAll()
        print()

owners = {}
for enterprise in enterprises:
    owner = enterprise.GetOwner()
    owners[owner] = owners.get(owner, 0) + 1

print("Власники, які мають більше одного підприємства:")
for owner, count in owners.items():
    if count > 1:
        print(owner)
