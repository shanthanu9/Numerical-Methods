def comb(n, i):
    num = 1
    den = 1

    for j in range(0, i):
        num *= (n-j)
        den *= j+1
    
    return num/den

def newton_forward_interpolation(x, y, x_pred):
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
    h = x[1] - x[0]         # Assuming equidistant x values
    u = (x_pred - x[0])/h

    # Maintaining a column of forward difference table
    # [Move ahead in the table in each iteration]
    fd_col = list(y)

    y_pred = 0
    for i in range(0, n):
        y_pred += comb(u, i) * fd_col[0]
        for j in range(0, n-i-1):
            fd_col[j] = fd_col[j+1] - fd_col[j]
    
    return y_pred

# Set of distint points
x = [1, 1.02, 1.04, 1.06, 1.08]
y = [0.242, 0.2371, 0.2323, 0.2275, 0.2227]

# Find interpolated value for
x_pred = 1.015

y_pred = newton_forward_interpolation(x, y, x_pred)
print('Interpolated value', y_pred)