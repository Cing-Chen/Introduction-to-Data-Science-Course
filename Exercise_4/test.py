import numpy as np

A = np.array([[1, 0], [0, 1]])
B = np.array([[1, 2], [3, 4], [5, 6]])

# print(A.shape)
# print(B.shape)

# print(A)
print(B)
print(B.transpose())

C = B.transpose()

# print(A[0, :])
# print(A[0, :].shape)
# print(B[1, :])
# print(B[1, :].shape)

print(B[1, :])
print(C[:, 1])

print(np.dot(A[0, :], B[1, :]))
print(np.dot(A[0, :], C[:, 1]))