import math

def taylor_poly(x,y):
    res = 0
    for i in range(0,n):
        res += h**i/math.factorial(i+1)*f[i](x,y)
    return res

def taylor():
    x=0
    y=y0
    print('approximations for order',n)
    for i in range(0,N+1):
        # print('N:',i,'x=',x,'is y=',y,'exact y=',y_exact(x,y),'abs error=',abs(y_exact(x,y)-y))
        print('N:',i,'x=',x,'is y=',y)
        y=y+h*taylor_poly(x,y)
        x=x+h

N = 10  # number of approximations to find
y0 = 1/2  # value of initial approximation at 0
h = 0.2  # common distance
n = 4  # order of taylor polynomial

# x and t are interchangeable, so are y and w

f = []

f.append(lambda x,y: y-x**2+1)  # function y' = f
f.append(lambda x,y: y-x**2+1-2*x)  # function y'' = f'
f.append(lambda x,y: y-x**2-2*x-1)  # function y''' = f''
f.append(lambda x,y: y-x**2-2*x-1) 

assert len(f)>=n, 'Coefficients of taylor polynomial do not match order' 

# actual value of function, used to compute error
y_exact = lambda x,y: (x+1)**2-0.5*math.e**x  

taylor()
