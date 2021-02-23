In [1]: import numpy as np

In [2]: n = 1000000

In [3]: x = np.linspace(0, 1, n+1)

In [4]: def sin_func(x):
   ...:     r = np.zeros_like(x)  # result
   ...:     for i in range(len(x)):
   ...:         r[i] = np.sin(x[i])
   ...:     return r
   ...:

In [5]: %timeit y = sin_func(x)
1 loops, best of 3: 2.68 s per loop

In [6]: %timeit y = np.sin(x)
10 loops, best of 3: 40.1 ms per loop