import numpy as np

v0 = 2
a = 0.2
dt = 0.1    # Increment
n = int(round(2/dt)) + 1    # No of t values
t_values = np.linspace(0, 2, n)
s_values = v0*t_values + 0.5*a*t_values**2

outfile = open('_12_output.txt', 'w')
outfile.write('# t   s(t)\n')           # write table header. Note: 'print' automatically adds a newline \n, but 'outfile.write(s)' must manually contain \n in 's'
for t, s in zip(t_values, s_values):
    outfile.write('%.2f %.4f\n' % (t, s))

# 'savetxt' - a convenient numpy package to save tabular data
# The data must be stored in a 2D numpy array.
# 'savetxt' enables to control the format of the numbers in each column (fmt)
# A header can be added, the header lines begin with a comment character

# Make 2D array of [t, s(t)] values in each row
data = np.array([t_values, s_values]).transpose()

# Write data array to file in table format
np.savetxt('_12_table.dat', data, fmt=['%.2f', '%.4f'], header='t    s(t)', comments='# ')

# Read the tabular data back into a numpy array:
# Line beginning with the comment character are skipped in the reading
# Resulting object is a 2D array: data[i,j]
data = np.loadtxt('_12_table.dat', comments='#')
print(data)