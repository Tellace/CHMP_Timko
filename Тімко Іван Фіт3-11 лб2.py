import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return 9*x**4 + 8*x**3 + 1.5*x**2 + 2*x - 10
    a = 1
    b = 2
    eps= 0.0001

def rec_dyhotomy(a, b, eps):
    if abs(f(b) - f(a)) < eps:
        print('Обчислюємо корінь')
        return
    mid = (a+b)/2
    if f(mid)==0 or abs(f(mid))<eps:
        print('Корінь знаходиться в точці x = {mid}')

    elif f(a)*f(mid)<0:
        rec_dyhotomy(a, mid, eps)
    else:
        rec_dyhotomy(mid, b, eps)

    x=np.arange(a, b, 0.01)

    plt.plot(x, f(x))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Метод ділення навпіл')
    plt.grid()
    plt.show()

# from scipy.misc import derivative

# def hord(a, b, eps):
#     if abs(b - a) < eps:
#          print("кореня немає")
#          return
#     if (f(a) * derivative(f, a, n=2)):
#         x0 = a
#         xi = b
#     else:
#         x0 = b
#         xi = a
#         xi_1 = xi - (xi - x0) * f(xi) / f(xi) - f(x0)
#     while (abs(xi_1 - xi) > eps):
#         xi = xi_1
#         xi_1 = xi - (xi - x0) * f(xi) / f(xi) - f(x0)

#     else:
#           print(f"Корінь знаходиться у точці x=", xi_1)
#         hord(a, b, eps)
