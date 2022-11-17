import numpy as np
from math import factorial

x=[1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465]
y=[0.8885, 0.8895, 0.8906, 0.8916, 0.8926, 0.8936, 0.8947, 0.8956, 0.8966, 0.8976, 0.8986]
h = x[1] - x[0]
x1=1.416
x2=1.456
q=(x1 - x[0])/h
q1 = (x2-x[-1])/h
def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)

s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)

n_1 = s_1 + s_2 + s_3 + s_4
print('the value of a function at a point x=',x1,'first formula',round(n_1,5))

x=[1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465]
y=[0.8885, 0.8895, 0.8906, 0.8916, 0.8926, 0.8936, 0.8947, 0.8956, 0.8966, 0.8976, 0.8986]
h = x[1] - x[0]
x1=1.416
x2=1.456
q=(x1 - x[0])/h
q1 = (x2-x[-1])/h
def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)

s_1 = y[0]+q*n(y,1)[0]+q*(q+1)*n(y,2)[0]/factorial(2)
s_2 = q*(q+1)*(q+2)*n(y,3)[0]/factorial(3)
s_3 = q*(q+1)*(q+2)*(q+3)*n(y,4)[0]/factorial(4)
s_4 = q*(q+1)*(q+2)*(q+3)*(q+4)*n(y,5)[0]/factorial(5)

n_2 = s_1 + s_2 + s_3 + s_4



print('the value of a function at a point x=',x1,'second formula',round(n_2,5))
