def double_each_element(l):    
    n = len(l)
    l_new = []
    for i in range(n):
        l_new.append(l[i])
        l_new.append(l[i])
    return l_new

def hermite_interpolation(x, y, y_red, x_pred):
    """
    Arguments
    ---------
    x: list
        x values
    y: list
        y value
    y_der: list
        y derivative values
    x_pred: float
        x value for which y value is being predicted
    """
    if len(x) != len(y):
        raise ValueError("x and y shape don't match")

    z = double_each_element(x)
    n = len(z)

    # Maintaining a column of divided difference table
    # [Move ahead in the table in each iteration]
    dd_col = double_each_element(y)
    for j in range(0, n-1):
        if j%2 == 0:
            dd_col[j] = y_der[j//2]
        else:
            dd_col[j] = (dd_col[j+1] - dd_col[j])/(z[j+1] - z[j])

    z_coef = (x_pred - z[0])
    y_pred = y[0]
    for i in range(1, n):
        y_pred += z_coef * dd_col[0]
        z_coef *= (x_pred - z[i])
        for j in range(0, n-i-1):
            dd_col[j] = (dd_col[j+1] - dd_col[j])/(z[j+i+1] - z[j])
    
    return y_pred

# This code is for Hermite interpolation using Newton divided
# difference approximation
# Set of distint points
x = [1.3, 1.6, 1.9]
y = [0.6200860, 0.4554022, 0.2818186]
y_der = [-0.5220232, -0.5698958, -0.5811571]

# Find interpolated value for
x_pred = 1.5

y_pred = hermite_interpolation(x, y, y_der, x_pred)
print('Interpolated value', y_pred)