# Lists collect a set of numbers or other objects in a single variable
L = ['mydata.txt', 3.14, 10]
print(L)
print(L[0])
print(L[1])
del(L[0])
print(L)
print(len(L))
L.append(-1)
print(L)

# Example 1
v0 = 2
a = 0.2
dt = 0.1
t = 0
t_values = []
s_values = []
while t <= 2.1:
    s = v0*t + 0.5*a*t**2
    t_values.append(t)
    s_values.append(s)
    t = t + dt
print(s_values)
print(t_values)

# Print a nicely formatted table
i = 0
while i <= len(t_values)-1:
    print('%.2f %.4f' % (t_values[i], s_values[i]))
    i += 1