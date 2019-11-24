import matplotlib.pyplot as plt
import numpy as np
import math
deg = 24
points = np.random.rand(2**deg + 1, 2)
dist = np.sum((points-0.5)**2, axis = -1)
mask = dist < 0.25
count = [np.count_nonzero(mask[:2**i]) for i in range(10, deg + 1)]
pi_exp = np.array([count[i-10]/2**i * 4 for i in range(10, deg + 1)])
print(pi_exp)
error = np.abs(math.pi - pi_exp)
print(error)
def pi_error(N, pi):
    return (pi/4*(1 - pi/4) / N)**0.5
xs = [2**k for k in range (10,deg + 1)]
ys = [pi_error(x, pi_exp[-1]) for x in xs]
print(ys)
plt.scatter(xs, error)
plt.plot(xs, error)
plt.plot(xs, ys)
plt.xscale('log')
plt.xlabel('Число измерений')
plt.ylabel('Ошибка измерений')
plt.show()