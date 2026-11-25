
import math
import matplotlib.pyplot as plt

x = [i / 100 for i in range(-200, 501)]
y = [math.exp(i) * math.sin(i) for i in x]

plt.plot(x, y, linestyle='-.', color='yellow')

plt.title('y = e^x sin x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.savefig('exponent.png')
plt.show()
