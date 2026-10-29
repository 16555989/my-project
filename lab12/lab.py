
import math

def square_roots(a, b, c):
    if a == 0:
        print("Це не квадратне рівняння.")
        return

    d = b ** 2 - 4 * a * c

    if d < 0:
        print("Дійсних коренів немає.")
    elif d == 0:
        print("x =", -b / (2 * a))
    else:
        print("x1 =", (-b + math.sqrt(d)) / (2 * a))
        print("x2 =", (-b - math.sqrt(d)) / (2 * a))

def biquadratic_roots(a, b, c):
    # a*x^4 + b*x^2 + c = 0
    square_roots(a, b, c)

    d = b ** 2 - 4 * a * c
    if a == 0 or d < 0:
        return

    for t in (
        (-b + math.sqrt(d)) / (2 * a),
        (-b - math.sqrt(d)) / (2 * a)
    ):
        if t > 0:
            print("x =", math.sqrt(t))
            print("x =", -math.sqrt(t))
        elif t == 0:
            print("x = 0")

print("Квадратне рівняння:")
square_roots(1, -5, 6)

print("Біквадратне рівняння:")
biquadratic_roots(1, -5, 4)
