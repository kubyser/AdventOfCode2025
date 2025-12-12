import numpy as np

A = np.array([[0, 0, 0, 0, 1, 1],
              [0, 1, 0, 0, 0, 1],
              [0, 0, 1, 1, 1, 0],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 1, 0, 0, 0]])
y = np.array([3, 5, 4, 7, 0, 0])

x = np.linalg.solve(A, y)
print(x)