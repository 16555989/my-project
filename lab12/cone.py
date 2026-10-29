
import math

def surface_area(R, r, h):
    l = math.sqrt(h ** 2 + (R - r) ** 2)
    return math.pi * (R ** 2 + r ** 2) + math.pi * (R + r) * l

def volume(R, r, h):
    return math.pi * h * (R ** 2 + R * r + r ** 2) / 3
