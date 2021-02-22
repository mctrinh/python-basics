v0 = 2
a = 0.2
dt = 0.1    # Increment
t = 0       # Start value
while t <= 2:
    s = v0*t + 0.5*a*t**2
    print('%.1f' %t, '%.3f' %s)
    t += dt

# Note: value at t = 2.0 is not printed out due to ifinitesimal error of t += dt
# Fixed: use while t <= 2.1