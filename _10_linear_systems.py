import numpy as np

A = np.array([[1., 2], [4, 2]])
b = np.array([1., -2])
x = np.linalg.solve(A, b)
print(x)

# Large matrix with special sparse structures
# Python has sparse matrix package 'scipy.sparse' can be used to construct various types of sparse matrices
# 'scipy.sparse.spdiags' can construct a sparse matrix form a few vectors representing the diagonals in the matrix
# all the diagonals must have the same length as the dimension of their sparse matrix
# Thus, some elements of the diagonals are not used:
#       the first 'k' elements are not used of the 'k' super-diagonal
#       the last 'k' elements are not used of the '-k' sub-diagonal.

# Ex: Construct a tridiagonal matrix
from scipy.sparse import spdiags
N = 6
diagonals = np.zeros((3, N))    # 3 diagonals
diagonals[0,:] = np.linspace(-1, -N, N)
diagonals[1,:] = -2
diagonals[2,:] = np.linspace(1, N, N)
A = spdiags(diagonals, [-1, 0, 1], N, N).toarray()      # .toarray to look at corresponding dense matrix    
print(A)

data = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
diags = np.array([0, -1, 2])
B = spdiags(data, diags, 4, 4).toarray()
print(B)

# A, x are given, compute b = Ax using the sparse matrix vector product associated with the sparse matrix A, then solve Ax = b
x = np.linspace(-1, 1, N)   # choose solution
b = A.dot(x)
print(x)
print(b)

from scipy.sparse.linalg import spsolve
x = spsolve(A, b)
print(x)

# Converting the linear system to its dense counterpart
A_d = spdiags(diagonals, [-1, 0, 1], N, N).toarray()            # corresponding dense matrix
b = np.dot(A_d, x)                                              # standard matrix vector product
x = np.linalg.solve(A_d, b)
print(x)