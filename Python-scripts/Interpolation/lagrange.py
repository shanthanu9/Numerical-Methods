from math import log

def L(n, k):
    """
    Lagrange Coefficient Polynomial
    """
    num = 1
    den = 1
    for i in range(n):
        if i != k:
            num *= (x_pred - x[i])
            den *= (x[k] - x[i])
    return num/den

def lagrange_interpolation(x, y, x_pred):
    """
    Arguments
    ---------
    x: list
        x values
    y: list
        y value
    x_pred: float
        x value for which y value is being predicted
    """
    if len(x) != len(y):
        raise ValueError("x and y shape don't match")

    n = len(x)
    y_pred = 0
    for i in range(0, n):
        # print('Coeff at', i, ':', L(n,i))
        y_pred += y[i] * L(n, i)
    
    return y_pred

# Set of distint points
# x = [300, 304, 305, 307]
# y = [2.4771, 2.4829, 2.4843, 2.4871]

x = [1,1.1,1.3,1.4]
y = [log(xi) for xi in x]

# Find interpolated value for
x_pred = 301

y_pred = lagrange_interpolation(x, y, x_pred)
print('Interpolated value', y_pred)