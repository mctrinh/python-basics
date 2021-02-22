t = 0.5
v0 = 2
a = 0.2
s = v0*t + 0.5*a*t**2
print(s)

# Output is specified as a string, %g implies a real number as compactly as possible 
print('s=%g' % s)

# Control the number of decimals
print('s=%.2f' % s)
print('s\t = \t %.3f' % s)

# Format string syntax
print('s={s:.2f}'.format(s=s))
