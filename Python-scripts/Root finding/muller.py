from cmath import sqrt

def muller(f, x0, x1, x2, tol, N):
    """
    Arguments
    ---------
    f: function
        function `f` to find root of
    x0, x1, x2: complex/float
        Initial 3 guesses of root
    tol: float 
        tolerance
    n: int
        maximum number of iterations
    """
    print('x0:',x0, '\nx1:', x1, '\nx2:', x2)
    n = 1
    while n <= N:
        h1 = x1 - x0
        h2 = x2 - x1
        δ1 = (f(x1)-f(x0))/h1
        δ2 = (f(x2)-f(x1))/h2

        # Coefficients of parabola (as quadratic eqn)
        d = (δ2 - δ1)/(h2 + h1)
        a = d                   # corresponds to a
        b = δ2 + h2*d           # corresponds to b
        c = f(x2)               # corresponds to c
        D = sqrt(b**2 - 4*f(x2)*d)      # corresponds to (b^2-4ac)^0.5
        E = b+D if abs(b-D) < abs(b+D) else b-D
        
        # Root approximation
        h = -2*f(x2)/E
        x = x2 + h

        print('Iteration', n, 'x', x, 'f(x)', f(x))
        if abs(h) < tol:
            break
        n += 1 
        # Update sequence variables
        x0 = x1
        x1 = x2
        x2 = x 
    return x2


## Using muller's method

from math import inf

f = lambda x: x**3 - 5*x - 1
x0 = 0
x1 = 0.5
x2 = 1
tol = 1e-6
n = 10

root = muller(f, x0, x1, x2, tol, n)
print('root', root)