import numpy as np
import matplotlib.pyplot as plt


x=np.array([-2.,-1.,0.,1. ],dtype = float)
y=np.array([-7.,4.,1.,2.],dtype=float)
def lagranz(x,y,t):
    z=0
    for j in range(len(y)):
        p1=1 ; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1 ; p2*1
            else:
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z
xnew = np.linspace(np.min(x),np.max(x),100)
ynew = [lagranz(x,y,i) for i in xnew]
plt.plot(x,y,'o',xnew,ynew);plt.title('Lagrange Polynomial_1');plt.grid(True);plt.show()