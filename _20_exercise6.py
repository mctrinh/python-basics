import numpy as np
import matplotlib.pyplot as plt

g = []
y = np.linspace(0,4,501)
for i in range(501):
    g.append(np.exp(-y[i])*np.sin(4*y[i]))
print(np.shape(y))
print(np.shape(g))
plt.figure(1)
plt.plot(y,g,'r-')
plt.xlabel('$y$')
plt.ylabel('$g(y)$')
plt.title('Damped sine wave')
plt.savefig('_20_exercise6.png')
plt.savefig('_20_exercise6.pdf')
plt.show()

def h(y):
    return np.exp(-1.5*y)*np.sin(4*y)

print(np.shape(h(y)))
plt.figure(2)
plt.plot(y,g,'r-')
plt.plot(y,h(y),'k--')
plt.legend(['g(y)', 'h(y)'])
plt.xlabel('$y$')
plt.ylabel('$Values$')
plt.title('Damped sine wave')
plt.savefig('_20_exercise7.png')
plt.savefig('_20_exercise7.pdf')
plt.show()