import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("start.txt", "r", encoding="utf-8")
countries = {}

for line in f:
    name, area = line.strip().split(":")
    countries[name.strip()] = float(area.strip())

f.close()

f = open("countries.txt", "w", encoding="utf-8")
for name in countries:
    f.write(name + "\n")
f.close()

f = open("squares.txt", "w", encoding="utf-8")
for area in countries.values():
    f.write(str(area) + "\n")
f.close()

largest = max(countries, key=countries.get)

f = open("largest.txt", "w", encoding="utf-8")
f.write(largest + ": " + str(countries[largest]))
f.close()