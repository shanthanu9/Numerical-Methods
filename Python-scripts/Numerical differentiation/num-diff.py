def two_point_first_der(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>Two point first der')
    print('>>>>Forward')
    for i in range(0,n-1):
        der=(y[i+1]-y[i])/h
        print(x[i], ':', der)
    print(x[-1], ':', 'Null')
    print('>>>>Backward')
    print(x[0], ':', 'Null')
    for i in range(1,n):
        der=(y[i]-y[i-1])/h
        print(x[i], ':', der)

def three_point_LEP(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>Three point LEP first der')
    for i in range(0,n-2):
        der=(-3*y[i]+4*y[i+1]-y[i+2])/(2*h)
        print(x[i], ':', der)
    for i in range(n-2, n):
        print(x[i], ':', 'Null')

def three_point_REP(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>Three point REP first der')
    for i in range(0, 2):
        print(x[i], ':', 'Null')
    for i in range(2,n):
        der=(-3*y[i]+4*y[i-1]-y[i-2])/(2*-h)
        print(x[i], ':', der)

def three_point_midpoint(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>Three point midpoint first der')
    for i in range(0, 1):
        print(x[i], ':', 'Null')
    for i in range(1,n-1):
        der=(-y[i-1]+y[i+1])/(2*h)
        print(x[i], ':', der)
    for i in range(n-1, n):
        print(x[i], ':', 'Null')

def five_point_LEP(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>five point LEP first der')
    for i in range(0,n-4):
        der=(-25*y[i]+48*y[i+1]-36*y[i+2]+16*y[i+3]-3*y[i+4])/(12*h)
        print(x[i], ':', der)
    for i in range(n-4, n):
        print(x[i], ':', 'Null')

def five_point_REP(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>five point REP first der')
    for i in range(0, 4):
        print(x[i], ':', 'Null')
    for i in range(4,n):
        der=(-25*y[i]+48*y[i-1]-36*y[i-2]+16*y[i-3]-3*y[i-4])/(12*-h)
        print(x[i], ':', der)

def five_point_midpoint(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>five point midpoint first der')
    for i in range(0, 2):
        print(x[i], ':', 'Null')
    for i in range(2,n-2):
        der=(y[i-2]-8*y[i-1]+8*y[i+1]-y[i+2])/(12*h)
        print(x[i], ':', der)
    for i in range(n-2, n):
        print(x[i], ':', 'Null')

def three_point_midpoint_double_der(x, y):
    '''
    x: list of equally spaced values
    y: list of function values evaluated at each x
    '''
    n=len(x)
    h=x[1]-x[0]
    print('>>>>Three point midpoint double der')
    for i in range(0, 1):
        print(x[i], ':', 'Null')
    for i in range(1,n-1):
        der=(y[i-1]-2*y[i]+y[i+1])/(h**2)
        print(x[i], ':', der)
    for i in range(n-1, n):
        print(x[i], ':', 'Null')

x=[1,1.05,1.1,1.15,1.2,1.25]
y=[0.682689,0.706282,0.728668,0.749856,0.769861,0.788700]
assert len(x)==len(y), 'len of x and y are not equal'

two_point_first_der(x,y)
three_point_LEP(x,y)
three_point_midpoint(x,y)
three_point_REP(x,y)
five_point_LEP(x,y)
five_point_midpoint(x,y)
five_point_REP(x,y)
three_point_midpoint_double_der(x,y)
