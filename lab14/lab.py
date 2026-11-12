
import urllib.request
from html.parser import HTMLParser
import json

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value:
                    self.count += 1

n = int(input("Введіть кількість вебсторінок (5-10): "))

while n < 5 or n > 10:
    n = int(input("Потрібно ввести число від 5 до 10: "))

results = {}

for i in range(n):
    url = input(f"Введіть URL вебсторінки {i + 1}: ")

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            html = response.read().decode(
                "utf-8", errors="ignore"
            )

        parser = MyParser()
        parser.feed(html)

        results[url] = parser.count

        print("Кількість гіперпосилань:", parser.count)

    except Exception as e:
        results[url] = "Помилка завантаження"
        print("Помилка:", e)

with open("links.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

print("Результати записано у файл links.json")
