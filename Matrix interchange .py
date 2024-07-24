import numpy as np

r, c = map(int, input().split())
matrix = np.zeros((r, c), dtype=int)

for i in range(r):
    matrix[i] = list(map(int, input().split()))

for i in range(r):
    matrix[i][0], matrix[i][c-1] = matrix[i][c-1], matrix[i][0]

for row in matrix:
    print(' '.join(map(str, row)))
