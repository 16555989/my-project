
import json
import os

filename = "database.json"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    data = []

def add_record():
    name = input("Введіть назву запису: ")
    category = input("Введіть категорію: ")
    data.append({"name": name, "category": category})

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Запис додано.")

def search_records():
    criterion = input("Введіть критерій пошуку: ")
    value = input("Введіть значення: ")

    for record in data:
        if str(record.get(criterion, "")) == value:
            print(record)

add_record()
search_records()
