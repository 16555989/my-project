
import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name('input.csv')

df = pd.read_csv(file_path, header=None)

df = df.apply(pd.to_numeric)

totals = df.sum()

for i, total in enumerate(totals, start=1):
    print(f'Фірма {i}: {total} покришок')
