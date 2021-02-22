import numpy as np
import matplotlib.pyplot as plt

def s(t):
    return v0*t + 0.5*a*t**2
# v0, a are global variables - must be defined before calling the s(t) function
# t is function argument
v0 = 0.2
a = 4
# Call the function
value = s(3)
print(value)

# Instead of having v0 and a as global variables, can let them be function arguments
def s1(t, v0, a):
    return v0*t + 0.5*a*t**2
# Call the function
value = s1(3, 0.2, 4)
print(value)
# More readable call
value = s1(t=3, v0=0.2, a=4)
print(value)

# Can declare functions arguments to have a default value, 
# allow to drop the argument in the call if the default value is appropriate
# called 'keyword arguments' or 'default arguments'
def s2(t, v0=1, a=1):
    return v0*t + 0.5*a*t**2
value = s2(3, 0.2, 4)       # specify new v0 and a
value = s2(3)               # rely on v0=1 and a=1
value = s2(3, a=2)          # rely on v0=1
value = s2(3, v0=2)         # rely on a=1
value = s2(t=3, v0=2, a=2)  # specify everything
value = s2(a=2, t=3, v0=2)  # any sequence allowed

# Vectorized functions
# Applying the function s(t, v0, a) to an array 't' can be done in 2 ways:
# Scalar code: work with one element at a time
# for i in range(len(t)):
#    s_values[i] = s(t_values[i], v0, a)

# Vectorized code: apply s to the entire array
# s_values = s(t_values, v0, a) 
# s must contain statements that work correctly when t is an array argument
# Vectorized code to avoid a loop in Python, but carry out math operations on entire arrays
# Technically, such (binary) operations are executed as loops in very as (compiled) C code.

# A function can return more than 1 value, say s(t) and v(t) = v0 + a*t
def movement(t, v0, a):
    s = v0*t + 0.5*a*t**2
    v = v0 + a*t
    return s, v
s_value, v_value = movement(t=0.2, v0=2, a=4)
print('s = %.4f, v = %.4f' % (s_value, v_value))

# Python function return only one object
# Even when we return several values such as s, v, actually only one object is returned.
# s, v values are packed together in a 'tuple' object (similar to a list)
# 'tuples' are constant lists, so you can index them as lists, but cannot change the contents ('append' or 'del' is illegal)
def f(x):
    return x+1, x+2, x+3
r = f(3)                    # Store all returned values in one object r
print(r)
print(type(r))
print(r[1])

# IF
def s_func(t, v0, a0, t1):
    if t <= t1:
        s = v0*t + 0.5*a0*t**2
    else:
        s = v0*t + 0.5*a0*t1**2 + a0*t1*(t-t1)
    return s
print(s_func(1, 1, 2, 3))
print(s_func(3,1,2,2))

# IF with 't' is an 'array' - ELEMENT-WISE loops
n = 201             # No of t values for plotting
t1 = 1.5
t = np.linspace(0, 2, n)
s = np.zeros(n)
for i in range(len(t)):
    s[i] = s_func(t=t[i], v0=0.2, a0=20, t1=t1)
plt.plot(t, s, 'b-')
plt.plot([t1, t1], [0, s_func(t=t1, v0=0.2, a0=20, t1=t1)], 'r--')
plt.plot([0, t1], [s_func(t=t1, v0=0.2, a0=20, t1=t1), s_func(t=t1, v0=0.2, a0=20, t1=t1)], 'r--')
plt.xlabel('t')
plt.ylabel('s')
plt.savefig('_8_functions.png')
plt.show()

# IF with VECTORIZATION avoid loop

# A vectorized if-else test can be coded using 'np.where'
# s = np.where(condition, s1, s2)
# 'condition' is an array of boolean values
# s[i] = s1[i] if condition [i] is True
# s[i] = s2[i] otherwise
a0 = 4
s = np.where(t <= t1, v0*t + 0.5*a0*t**2, v0*t + 0.5*a0*t1**2 + a0*t1*(t-t1))
# t <= t1 with array t and scalar t1 results in a boolean array b where b[i] = t[i] <= t1

# Using array indexing
# Possible to index a subset of indices in an array 's' using a boolean array b: s[b].
# This construction picks out all the elements s[i] where b[i] is True.
# On the right-hand side, we can then assign some array expression 'expr' of the same length as s[b]
# s[b] = (expr)[b]
# In the example, b is as t <= t1 and t >= t1
s = np.zeros_like(t)        # Make s as zeros, same size & type as t
s[t <= t1] = (v0*t + 0.5*a0*t**2)[t <= t1]
s[t > t1] = (v0*t + 0.5*a0*t1**2 + a0*t1*(t-t1))[t > t1]