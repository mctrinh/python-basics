import numpy as np

# 'b' is a VIEW of 'a', 'a' is changed 'b' is changed, vice versa
a = np.linspace(1, 5, 5)
b = a
print(a)
print(b)
b[0] = 5
print(a)
print(b)
a[1] = 9
print(a)
print(b)
# b[1:-1] is a view into subset of a
print(b[1:-1])
print(b[-1])
print(b[4])

# A 'COPY' of the array is required to change 'b' without affecting 'a'
c = a.copy()        # copy all elements to a new array c
c[0] = 6            # a is not changed
print(a)
print(b)
print(c)
b = a[1:-2].copy()
print(b)

a = np.array([-1, 4.5, 8, 9])
b = a[1:-2]                     # view: changes in a are reflected in b
b = a[1:-2].copy()              # copy: changes in a are not reflected in b
