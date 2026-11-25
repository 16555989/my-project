
import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name('text.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = pd.Series(text.split())

vowels = 'аеєиіїоуяюАЕЄИІЇОУЯЮ'

result = words[
    words.apply(lambda word: sum(1 for letter in word if letter in vowels) >= 3)
]

output_path = Path(__file__).with_name('result.txt')
result.to_csv(output_path, index=False, header=False)

print('Слова з трьома і більше голосними:')
print(result.to_string(index=False))
print('Результат збережено у result.txt')
