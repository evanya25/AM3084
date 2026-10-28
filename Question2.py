import numpy as np

A = np.array([[2, 1, 1],
              [1, 3, 2],
              [3, 1, 2]])

B = np.array([10, 18, 17])

print("Determinant =", np.linalg.det(A))
print("Inverse =")
print(np.linalg.inv(A))

print("Eigenvalues =")
print(np.linalg.eigvals(A))

print("Eigenvectors =")
print(np.linalg.eig(A)[1])

X = np.linalg.solve(A, B)
print("Solution =", X)

R = np.dot(A, X) - B
print("Residual =", R)
print("Residual norm =", np.linalg.norm(R))