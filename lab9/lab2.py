A = set(range(2, 201, 2))
B = set(range(3, 301, 3))
C = set(range(5, 501, 5))

print("1)", sorted(A & B & C))
print("2)", sorted((B & C) - A))
print("3)", sorted(C - A - B))