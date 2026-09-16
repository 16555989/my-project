import math

# Введення значення x з клавіатури
x = float(input("Введіть x: "))

# Обчислення значення y залежно від умови
if x > 7:
    y = 2.27 * math.exp(4 * x + 1) + 3
elif x > 0.5:
    y = 0.64 * x**(4 * x + 0.1)
else:
    # Оскільки log за замовчуванням у Python є натуральним (ln)
    y = math.log(abs(x - math.e))

# Виведення результату
print(f"y = {y}")
