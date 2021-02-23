n = 20
for i in range(n+1):
    print('x%d=%d' % (i, i**2 + 1))

x=[]
for i in range(21):
    x.append(i**2 + 1)
print(x)

x = [i**2 + 1 for i in range(21)]
print(x)

def f(n):
    return n**2 + 1
print(f(4))

