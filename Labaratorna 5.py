import numpy as np 

from scipy import optimize 

from scipy .misc import derivative 

import math 

x0 = 0.510 

y0 = -0.201 

delta = 0.1 

 

def f1(y): 

return -math.sin(-y)+1.2 

def f2(x): 

return 1+math.cos(x)/2 

 

def iter(x, y, e): 

xn = x 

yn = y 

xn1 = f2(x) 

yn1 = f1(y) 

n = 1 

while ((abs(xn1-xn)>=e)&(abs(yn1-yn)>=e)): 

xn=xn1 

yn=yn1 

yn1=f1(xn) 

xn1=f2(yn1) 

n+=1 

print('Simple iteration:') 

print('x=', xn, '\ny=', yn, '\nThe amount ofiteration=', n) 

iter(x0, y0,0.001) 

 

def f3(x): 

return math.cos(x[0])+x[1]-1.5, 2*x[0]-math.sin(x[1]-0.5)-1 

s=optimize.root(f3,[0.,0.],method='hybr') 

print('Chek',s.x) 