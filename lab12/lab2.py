
def remove_protocol(url):
    if url.startswith("https://"):
        return url[8:]
    elif url.startswith("http://"):
        return url[7:]
    return url

n = int(input("Введіть кількість сайтів: "))
sites = []

for i in range(n):
    url = input("Введіть URL сайту: ")
    sites.append(remove_protocol(url))

print("Список адрес без протоколу:")
for site in sites:
    print(site)
