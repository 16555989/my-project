
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path
import re

# Відкриття текстового файлу
file_path = Path(__file__).with_name('text.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read().lower()

# Пошук слів у тексті
words = re.findall(r'[а-яіїєґ]+', text)

# Підрахунок частоти слів
frequency = Counter(words)

# Побудова вертикальної гістограми
plt.bar(frequency.keys(), frequency.values())

plt.title('Частота появи слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Кількість повторень')
plt.xticks(rotation=45)
plt.tight_layout()

# Виведення гістограми
plt.show()
