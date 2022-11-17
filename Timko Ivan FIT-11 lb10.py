import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial
from math import factorial
def taylor(x):
    y = 0
    d1 = sp.diff(f,x)
    d2 = sp.diff(d1,x)
    d3 = sp.diff(d2,x)
    print('d1=',d1,'d2=',d2,'d3=',d3)
    y += f+d1*x+d2*(x*4)**2/factorial(2)+d3*(x+1)**3/factorial(3)
    print('y=',y)

    return y
x = sp.symbols('x')
f = sp.sin(sp.cos(x))
taylor_x = taylor(x)

sp.plot(taylor_x,f,(x,-1,1), label='Talor')

for degree in np.arange(1,15,step=2):
    series_t = approximate_taylor_polynomial(np.cos(3*x-1)+x, 0,degree,1,order=degree+2)
    plt.plot(x,series_t)
    plt.axis([-10,10,-10,10])
    plt.show()