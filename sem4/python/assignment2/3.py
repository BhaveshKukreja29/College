import numpy as np

def read_matrix():
    r, c = map(int, input("Enter rows and columns: ").split())
    print("Enter matrix elements row-wise:")
    return np.array([list(map(int, input().split())) for _ in range(r)])

m1 = read_matrix()
m2 = read_matrix()

if m1.shape[1] == m2.shape[0]:  # Matrix multiplication condition
    result = np.dot(m1, m2)
    print("Matrix Multiplication Result:\n", result)
else:
    print("Matrix multiplication not possible.")

print("Diagonal elements of first matrix:", np.diag(m1))
print("Diagonal elements of second matrix:", np.diag(m2))

if m1.shape[0] == m1.shape[1]:
    print("First matrix is a square matrix.")
else:
    print("First matrix is NOT a square matrix.")
