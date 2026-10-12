import random

M = int(input("Введіть M: "))
N = int(input("Введіть N: "))

A = []
B = []

for i in range(M):
    A.append([random.randint(1, 50) for j in range(N)])
    B.append([random.randint(1, 50) for j in range(N)])

print("Масив A:")
for row in A:
    print(row)

print("Масив B:")
for row in B:
    print(row)

print("Сума:")
for i in range(M):
    print([A[i][j] + B[i][j] for j in range(N)])

print("Різниця:")
for i in range(M):
    print([A[i][j] - B[i][j] for j in range(N)])

print("Добуток:")
for i in range(M):
    print([A[i][j] * B[i][j] for j in range(N)])