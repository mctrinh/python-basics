L = [1, 4, 8, 9]
for e in L:
    print(e)

list1 = [0, 0.1, 0.2]
list2 = []
for element in list1:
    p = element + 2
    list2.append(p)
print(list2)

# To work with somelist[i] use
# for i in range(len(somelist)):
# range(a, b, s) returns the integers a, a+s, a+2*s, ... up to but not including b
# range(b) implies a = 0, s = 1

# Need loop over 0, 0.1, 0.2, ..., 1
values = []
for i in range(11):
    values.append(i*0.1)
print(values)

# Shorter version using list comprehension (same as the loop above)
values = [i*0.1 for i in range(11)]
print(values)

# To work with value use
# for value in values:

# Example 1
v0 = 2
a = 0.2
dt = 0.1
t_values = []
s_values = []
n = int(round(2/dt)) + 1    # No of t values
for i in range(n):
    t = i*dt
    s = v0*t + 0.5*a*t**2
    t_values.append(t)
    s_values.append(s)
print(s_values)     # Just take a look at a created list

# Make nicely formatted table
# zip construction to run through multiple lists simultaneously
# for e1, e2, e3, ... in zip(list1, list2, list3, ...):
for t, s in zip(t_values, s_values):
    print('%.2f %.4f' % (t, s))

# Alternative implementation
# create a for loop over all the legal index values and index each array
# for i in range(len(list)):
#     e1 = list1[i]
#     e2 = list2[i]
for i in range(len(t_values)):
    print('%.2f %.4f' % (t_values[i], s_values[i]))


