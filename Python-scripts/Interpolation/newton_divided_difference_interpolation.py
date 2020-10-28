def newton_divided_difference_interpolation(x, y, x_pred):
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

    # Maintaining a column of divided difference table
    # [Move ahead in the table in each iteration]
    dd_col = list(y)

    x_coef = 1
    y_pred = 0
    for i in range(0, n):
        y_pred += x_coef * dd_col[0]
        x_coef *= (x_pred - x[i])
        for j in range(0, n-i-1):
            dd_col[j] = (dd_col[j+1] - dd_col[j])/(x[j+i+1] - x[j])
    
    return y_pred

# Set of distint points
x = [0.5, 1.5, 3.0, 5.0, 6.5, 8.0]
y = [1.625, 5.875, 31.0, 131.0, 282.125, 521.0]

# Find interpolated value for
x_pred = 7

y_pred = newton_divided_difference_interpolation(x, y, x_pred)
print('Interpolated value', y_pred)