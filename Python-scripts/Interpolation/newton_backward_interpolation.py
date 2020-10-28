def comb(n, i):
    num = 1
    den = 1

    for j in range(0, i):
        num *= (n-j)
        den *= j+1
    
    return num/den

def newton_backward_interpolation(x, y, x_pred):    
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
    u = (x_pred - x[-1])/h

    # Maintaining a column of (reverse) backward difference table
    # [Move ahead in the table in each iteration]
    rbk_col = y[::-1]   # reverse
    print()

    y_pred = 0
    for i in range(0, n):
        y_pred += (-1)**i * comb(-u, i) * rbk_col[0]
        for j in range(0, n-i-1):
            rbk_col[j] = rbk_col[j] - rbk_col[j+1]
    
    return y_pred

# Set of distint points
x = [1, 1.05, 1.10, 1.15, 1.20, 1.25]
y = [0.682689, 0.706282, 0.728668, 0.749856, 0.769861, 0.788700]

# Find interpolated value for
x_pred = 1.235

y_pred = newton_backward_interpolation(x, y, x_pred)
print('Interpolated value', y_pred)