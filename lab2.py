s = input("Введіть рядок слів: ")

words = s.split()
longest = max(words, key=len)

print("Найдовше слово:", longest)
print("Довжина слова:", len(longest))