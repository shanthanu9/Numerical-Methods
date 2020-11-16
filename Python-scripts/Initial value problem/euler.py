import math

def euler():
    x=0
    y=y0
    print('approximations:')
    for i in range(0,N+1):
        print('N:',i,'x=',x,'is y=',y,'exact y=',y_exact(x,y),'abs error=',abs(y_exact(x,y)-y))
        # print('N:',i,'x=',x,'is y=',y)
        y=y+h*f(x,y)
        x=x+h

N = 10  # number of approximations to find
y0 = 1/2  # value of initial approximation at 0
h = 0.1  # common distance

f = lambda x,y: y-x  # function such that y' = f

# actual value of function, used to compute error
y_exact = lambda x,y: x+1-0.5*math.e**x  

euler()