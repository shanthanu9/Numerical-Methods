import math

# <<<<<<<< RUNGE KUTTA METHOD OF ORDER TWO (MIDPOINT METHOD)

def runge_kutta_order2():
    x=0
    y=y0
    print('approximations:')
    for i in range(0,N+1):
        # print('N:',i,'x=',x,'is y=',y,'exact y=',y_exact(x,y),'abs error=',abs(y_exact(x,y)-y))
        print('N:',i,'x=',x,'is y=',y)
        y = y + h * f(x + h/2, y + h/2 * f(x,y))
        x = x + h

N = 10  # number of approximations to find
y0 = 1/2  # value of initial approximation at 0
h = 0.2  # common distance

# x and t are interchangeable, so are y and w
f = lambda x,y: y-x**2+1  # function such that y' = f

# actual value of function, used to compute error
y_exact = lambda x,y: (x+1)**2-0.5*math.e**x  
# runge_kutta_order2()

# <<<<<<<< MODIFIED EULER METHOD

def modified_euler():
    x=0
    y=y0
    print('approximations:')
    for i in range(0,N+1):
        # print('N:',i,'x=',x,'is y=',y,'exact y=',y_exact(x,y),'abs error=',abs(y_exact(x,y)-y))
        print('N:',i,'x=',x,'is y=',y)
        x_nxt = x + h
        y = y + h/2 * (f(x,y) + f(x_nxt, y + h*f(x,y)))
        x = x_nxt

N = 10  # number of approximations to find
y0 = 1/2  # value of initial approximation at 0
h = 0.2  # common distance

# x and t are interchangeable, so are y and w
f = lambda x,y: y-x**2+1  # function such that y' = f

# actual value of function, used to compute error
y_exact = lambda x,y: (x+1)**2-0.5*math.e**x
# modified_euler()

# <<<<<<<< HEUN METHOD

def heun():
    x=0
    y=y0
    print('approximations:')
    for i in range(0,N+1):
        # print('N:',i,'x=',x,'is y=',y,'exact y=',y_exact(x,y),'abs error=',abs(y_exact(x,y)-y))
        print('N:',i,'x=',x,'is y=',y)
        y = y + h/4 * (f(x,y) + 3*f(x + 2*h/3, y + 2*h/3 * f(x + h/3, y + h/3 * f(x,y))))
        x = x + h

N = 10  # number of approximations to find
y0 = 1/2  # value of initial approximation at 0
h = 0.2  # common distance

# x and t are interchangeable, so are y and w
f = lambda x,y: y-x**2+1  # function such that y' = f

# actual value of function, used to compute error
y_exact = lambda x,y: (x+1)**2-0.5*math.e**x
# heun()

# <<<<<<<< RUNGE KUTTA METHOD OF ORDER FOUR

def runge_kutta_order4():
    x=0
    y=y0
    print('approximations:')
    for i in range(0,N+1):
        # print('N:',i,'x=',x,'is y=',y,'exact y=',y_exact(x,y),'abs error=',abs(y_exact(x,y)-y))
        print('N:',i,'x=',x,'is y=',y)
        x_nxt = x + h
        k1 = h*f(x,y)
        k2 = h*f(x + h/2, y + k1/2)
        k3 = h*f(x + h/2, y + k2/2)
        k4 = h*f(x_nxt, y + k3) 
        y = y + 1/6*(k1 + 2*k2 + 2*k3 + k4)
        x = x_nxt

N = 10  # number of approximations to find
y0 = 1/2  # value of initial approximation at 0
h = 0.2  # common distance

# x and t are interchangeable, so are y and w
f = lambda x,y: y-x**2+1  # function such that y' = f

# actual value of function, used to compute error
y_exact = lambda x,y: (x+1)**2-0.5*math.e**x
runge_kutta_order4()
