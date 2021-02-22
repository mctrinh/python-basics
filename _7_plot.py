import numpy as np
import matplotlib.pyplot as plt

# Matlab user may prefer to do
# from numpy import *
# from matplotlib.pyplot import *
# such that they can use 'linspace' and 'plot' without any prefix as in Matlab

v0 = 0.2
a1 = 2
a2 = 8
n = 21      # No of t for plotting

t = np.linspace(0, 2, n)
s1 = v0*t + 0.5*a1*t**2
s2 = v0*t + 0.5*a2*t**2

plt.plot(t, s1, 'g', t, s2, '.b')
plt.xlabel('t')
plt.ylabel('s')
plt.title('Distance plot')
plt.legend(('$s(t; v_0=0.2, a=2)$', '$s(t;v_0=0.2, a=8)$'))
plt.savefig('_7_plot.png')
plt.show()