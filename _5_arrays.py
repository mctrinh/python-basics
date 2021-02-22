# 'Arrays' much like 'lists', but tailored for collection of numbers
# Advantage: can use them efficiently in mathematical computations
# Downside: have a fixed length and all elements must be of the same type
# 'Arrays' are available in the 'numpy' module
# Mathematical functions with arrays are element-wise
import numpy as np

L = [1, 4, 10.0]    # List of numbers
a = np.array(L)     # Make corresponding array
print(a)
print(a[1])
print(a.dtype)      # Data type of an element
b = 2*a + 1
print(b)
c = np.log(a)
print(c)

# Create n+1 uniformly distributed coordinates in [a,b], stored in an array, can use 'linspace'
# t = np.linspace(a, b, n+1)

v0 = 2
a = 0.2
dt = 0.1    # Increment
n = int(round(2/dt)) + 1    # No of t values

t_values = np.linspace(0, 2, n)
s_values = v0*t_values + 0.5*a*t_values**2

# Make nicely formatted table
for t, s in zip(t_values, s_values):
    print('%.2f %.4f' % (t, s))
print(t_values)