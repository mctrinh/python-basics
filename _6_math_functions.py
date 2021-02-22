# Module 'math' used for 'scalars' (single numbers)
import math                         # 1
from math import sin, pi            # 2
from math import *                  # 3. To import everything from 'math'
from numpy import *                 # 4. 'numpy' has functions can work on both scalars & arrays
import numpy as np                  # 5. Common in Python community
from numpy import sin, exp, pi      # 6

# 1
print(math.sin(math.pi))

# 2
print(sin(pi))

# 3
print(sin(pi), log(e), tanh(0.5))

# 4
x = linspace(0, 1, 101)
y = exp(-x)*sin(pi*x)

# 5
x = np.linspace(0, 1, 101)
y = np.exp(-x)*sin(np.pi*x)

# 6
x = np.linspace(0, 1, 101)
y = exp(-x)*sin(pi*x)
