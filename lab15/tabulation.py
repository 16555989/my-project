
import math

def tabulate(a, b, steps=100):
    result = []

    dx = (b - a) / steps

    for i in range(steps + 1):
        x = a + i * dx
        y = x ** 2 + math.sin(x)
        result.append((x, y))

    return result
