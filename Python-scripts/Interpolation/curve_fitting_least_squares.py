import numpy as np
from math import log

def curve_fit(x, y, deg=1):
    """
    Arguments
    ---------
    x: numpy.array
        x values
    y: numpy.array
        y value
    deg: int
        Degree of interpolated polynomial

    Returns
    -------
    np.array:
        Returns coefficients of polynomial
        [Starting from highest degree]
    """
    n = deg+1
    X = np.zeros((n, n))
    Y = np.zeros(n)

    # Initialize X
    for i in range(0, n):
        for j in range(0, n):
            X[i][j] = np.sum(x**(i+j))
    
    # Initialize Y
    for i in range(0, n):
        Y[i] = np.sum(y*x**(i))

    A =  np.linalg.solve(X, Y)

    # compute error
    error=0
    for i in range(len(x)):
        polyval=0
        for j in range(0,len(A)):
            polyval += A[j]*(x[i])**j
        # print('polyval',polyval)
        error += (y[i] - polyval)**2
    print('Error:', error)

    A= np.flip(A)
    return A

# Degree 2 example
# x = np.array([0, 0.25, 0.5, 0.75, 1.0])
# y = np.array([1.0000, 1.2840, 1.6487, 2.1170, 2.7183])
x = np.array([4,4.2,4.5,4.7,5.1,5.5,5.9,6.3,6.8,7.1])
y = np.array([102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.50,326.72])
y = np.array([log(yi) for yi in y])
deg = 1

A = curve_fit(x, y, deg)
print('Coefficients (highest power of x to lowest):', A)

# # Degree 1 (linear) example
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = np.array([1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6])

# A = curve_fit(x, y)
# print('Coefficients (highest power of x to lowest):', A)