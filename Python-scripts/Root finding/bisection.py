# Defining Function
def f(x):
    # Lecture example, give first guess = 1, second guess = 2
    return x**6 - x - 1

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        # uncomment this if you want function value to be within error
        # condition = abs(f(x2)) > e

        # here, root value is considered for error
        condition = abs(x1 - x0) > e and f(x2) != 0

    print('\nRequired Root is : %0.8f' % x2)


# First guess
x0 = 1.0
# Second guess
x1 = 2.0
# Error
e = 1e-3

# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)