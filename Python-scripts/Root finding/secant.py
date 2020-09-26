# Defining Function
def f(x):
    # Lecture example
    # initial x0=3, x1=3.5
    return x**3 - 8*x - 5

# Implementing Secant Method

def secant(x0,x1,e,N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        prev_x1 = x1
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        # uncomment this if you want function value to be within error
        # condition = abs(f(x2)) > e

        # here, root value is considered for error
        condition = abs(x2 - prev_x1) > e and f(x2) != 0

    print('\n Required root is: %0.8f' % x2)

# Initial guess
x0 = 3
x1 = 3.5
# Error
e = 1e-5
# Max iterations
N = 10

# Starting Secant Method
secant(x0,x1,e,N)
