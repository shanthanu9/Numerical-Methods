# <<<<<<<<<<< BASIC RULES

def trapezoidal_rule(x, y):
    assert len(x) == len(y) == 2
    h = x[1] - x[0]
    return (h/2)*(y[0] + y[1])

def simpson_one_third_rule(x, y):
    assert len(x) == len(y) == 3
    h = x[1] - x[0]
    return (h/3)*(y[0] + 4*y[1] + y[2])

def simpson_three_eighth_rule(x, y):
    assert len(x) == len(y) == 4
    h = x[1] - x[0]
    return (3*h/8)*(y[0] + 3*y[1] + 3*y[2] + y[3])

def boole_rule(x, y):
    assert len(x) == len(y) == 5
    h = x[1] - x[0]
    return (2*h/45)*(7*y[0] + 32*y[1] + 12*y[2] + 32*y[3] + 7*y[4])

# <<<<<<<<<<< COMPOSITE NEWTON COTE'S RULE

# <<<<<< Composite trapezoidal rule

def composite_trapezoidal_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-1):
        sum += trapezoidal_rule(x[i:i+2], y[i:i+2])
    return sum

x = [7.47, 7.48, 7.49, 7.50, 7.51, 7.52]
y = [1.93, 1.95, 1.98, 2.01, 2.03, 2.06]
# composite_trapezoidal_rule(x, y)

# <<<<<< Composite Simpson's one-third rule

def composite_simpson_one_third_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-2, 2):
        sum += simpson_one_third_rule(x[i:i+3], y[i:i+3])
    return sum

x = [0, 0.25, 0.5, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
y = [0.5, 0.4923, 0.4706, 0.4384, 0.4, 0.3596, 0.32, 0.2832, 0.25]
# composite_simpson_one_third_rule(x, y)

# <<<<<< Composite Simpson's three-eighth rule

def composite_simpson_three_eighth_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-3, 3):
        sum += simpson_three_eighth_rule(x[i:i+4], y[i:i+4])
    return sum

# <<<<<< Composite Boole's rule

def composite_boole_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-4, 4):
        sum += simpson_three_eighth_rule(x[i:i+5], y[i:i+5])
    return sum