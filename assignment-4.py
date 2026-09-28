import numpy as np

A = []
print("Enter elements for 2x2 Matrix A:")
for i in range(2):
    row = []
    for j in range(2):
        row.append(int(input("Enter number: ")))
    A.append(row)

B = []
print("Enter elements for 2x2 Matrix B:")
for i in range(2):
    row = []
    for j in range(2):
        row.append(int(input("Enter number: ")))
    B.append(row)

res = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        res[i][j] = A[i][j] + B[i][j]

print("Result using Lists:")
for row in res:
    print(row)

nA = np.array(A)
nB = np.array(B)
nRes = nA + nB

print("Result using NumPy:")
print(nRes)