import math

def runge_kutta_order4():
    # print('Runge kutta order 4')
    x=0
    y=y0
    res = [[0,y0]]
    for i in range(0,N+1):
        # print('N:',i,'x=',x,'is y=',y,'exact y=',y_exact(x,y),'abs error=',abs(y_exact(x,y)-y))
        # print('N:',i,'x=',x,'is y=',y)
        x_nxt = x + h
        k1 = h*f(x,y)
        k2 = h*f(x + h/2, y + k1/2)
        k3 = h*f(x + h/2, y + k2/2)
        k4 = h*f(x_nxt, y + k3) 
        y = y + 1/6*(k1 + 2*k2 + 2*k3 + k4)
        x = x_nxt
        
        if i<=k-2:
            res.append([x,y])
    return res

# <<<<<<<<<<<<<<<<<<< ADAM BASHFORTH EXPLICIT

def adam_explicit():
    res = runge_kutta_order4()
    x=[r[0] for r in res]
    y=[r[1] for r in res]

    print('Adam bashforth explicit ',k,'-step method:')
    for i in range(-1,len(x)-1):
        print('N:',i+1,'x=',x[i+1],'is y=',y[i+1],'exact y=',y_exact(x[i+1],y[i+1]),'abs error=',abs(y_exact(x[i+1],y[i+1])-y[i+1]))
        # print('N:',i+1,'x=',x[i+1],'is y=',y[i+1])

    for i in range(k-1,N):
        x.append(0)
        y.append(0)
        if k==2:
            y[i+1] = y[i] + h/2*(3*f(x[i],y[i])-f(x[i-1],y[i-1]))
        elif k==3:
            y[i+1] = y[i] + h/12*(23*f(x[i],y[i])-16*f(x[i-1],y[i-1])+5*f(x[i-2],y[i-2]))
        elif k==4:
            y[i+1] = y[i] + h/24*(55*f(x[i],y[i])-59*f(x[i-1],y[i-1])+37*f(x[i-2],y[i-2])-9*f(x[i-3],y[i-3]))
        x[i+1] = x[i]+h
        print('N:',i+1,'x=',x[i+1],'is y=',y[i+1],'exact y=',y_exact(x[i+1],y[i+1]),'abs error=',abs(y_exact(x[i+1],y[i+1])-y[i+1]))
        # print('N:',i+1,'x=',x[i+1],'is y=',y[i+1])


N = 10  # number of approximations to find
y0 = 1/2  # value of initial approximation at 0
h = 0.2  # common distance

# k = 2 : Adam bashforth two step
# k = 3 : Adam bashforth three step
# k = 4: Adam bashforth four step
# Uses runge kutta order 4 to approximate values from y0 to y_k-1
# and later uses adam explicit formula for y_k to y_N
k = 2

# x and t are interchangeable, so are y and w
f = lambda x,y: y-x**2+1  # function such that y' = f

# actual value of function, used to compute error
y_exact = lambda x,y: (x+1)**2-0.5*math.e**x
adam_explicit()