
import cone

R = float(input("Введіть більший радіус: "))
r = float(input("Введіть менший радіус: "))
h = float(input("Введіть висоту: "))

print("Площа поверхні:", cone.surface_area(R, r, h))
print("Об'єм:", cone.volume(R, r, h))
