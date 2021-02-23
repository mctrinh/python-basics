from math import cos, sin, pi

def f(x):
    f0 = cos(2*x)
    f1 = -2*sin(2*x)
    f2 = -4*cos(2*x)
    return f0, f1, f2
x = pi
print('f(x)=%.4f\nf\'(x)=%.4f\nf\'\'(x)=%.4f' % f(x))

def deriv2(x):
    return cos(2*x), -2*sin(2*x), -4*cos(2*x)
f, df, d2f = deriv2(x=pi)
print(f, df, d2f)

