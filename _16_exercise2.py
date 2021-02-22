def f(x):
    return x**2
x = 2.55
y = f(x)
print('y(%.3f) = %.3f' % (x, y))
from math import pi
print('y(%.3f) = %.3f' % (pi, f(pi)))