
import urllib.request
from html.parser import HTMLParser
import re
import json
from collections import Counter

class EmailParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.emails = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == "href" and value and value.startswith("mailto:"):
                email = value[7:].split("?")[0]
                self.emails.add(email.lower())

    def handle_data(self, data):
        found = re.findall(
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            data
        )
        for email in found:
            self.emails.add(email.lower())


url = input("Введіть URL вебсторінки: ")

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

    parser = EmailParser()
    parser.feed(html)

    servers = Counter(
        email.split("@")[1]
        for email in parser.emails
    )

    results = dict(servers)

    with open("mail.json", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print("Результати пошуку:")

    for server, count in results.items():
        print(server, "-", count)

    print("Результат записано у файл mail.json")

except Exception as e:
    print("Помилка завантаження:", e)
