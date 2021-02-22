infile = open('_11_input.txt', 'r')     # lines in file are string variables
for line in infile:
    # Typical line: variable = value
    variable, value = line.split('=')
    variable = variable.strip()         # remove leading/trailing blanks
    if variable == 'v0':
        v0 = float(value)
    elif variable == 'a':
        a = float(value)
    elif variable == 'dt':
        dt = float(value)
    elif variable == 'interval':
        interval = eval(value)          # eval(s) interprets the text in the string s as Python code, interval becomes a name of a list object with content [0, 2]
infile.close()
print(v0)
print(a)
print(dt)
print(interval)

# To split a line into words separated by a character '='
line = 'v0 = 5.2'
variable, value = line.split('=')

# More modern Python way of opening files:
with open('_11_input.txt', 'r') as infile:
    for line in infile:
        ...

