
import numpy as np

def jacobi(dim, A, B, X0, tol, n):
    """
    Arguments
    ---------
    dim: int
        Dimension of square matrix `A`
    A: 2D np.array
        Coefficient matrix
    B: np.array
        Constant matrix
    X0: np.array
        Initial approximation
    tol: float
        tolerance
    n: int
        maximum number of iterations
    """

    print('n:', 0, 'X:', X0)
    iterations = 1
    while iterations <= n:
        X1 = np.array(dim * [0.])
        for i in range(dim):
            for j in range(dim):
                X1[i] += (-A[i][j]*X0[j])
            X1[i] += A[i][i]*X0[i]
            X1[i] += B[i]
            X1[i] /= A[i][i]

        print('n:', iterations, 'X:', X1)

        if np.max(abs(X0 - X1)) < tol:
            break
        iterations += 1
        X0 = X1  
    return X1

A = np.array([
    [15, 3, -2],
    [2, 10, 1],
    [1, -2, 8]
    ], dtype=float)
B = np.array([85, 51, 5], dtype=float)

dim = A.shape[0]
tol = 1e-5
n = 10
init_approx = np.array(dim * [0.])

# check diagonal dominance
for i in range(dim):
    v1 = abs(A[i][i])
    s = 0
    for j in range(dim):
        if i != j:
            s += abs(A[i][j])
    if s > v1:
        print('A is not diagonally dominant. Change A and B accordingly')
        exit()

jacobi(dim, A, B, init_approx, tol, n)