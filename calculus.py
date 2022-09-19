import numpy as np
import matplotlib.pyplot as plt


def l_x(x):
    return 2 * (x-1)*(x-2)*(x-3)/-6 + x*(x-2)*(x-3)/2 + 0.4 * (x-1)*x*(x-3)/-2 + 0.2*(x-2)*(x-1)*x/6


def l1_x(x):
    return (-3 * x * (x - 1)) + (-1 * (x + 1) * (x - 1)) + ((x + 1) * x * 3)


def newt_x(x):
    return -6 + 7 * (x + 1) - 2 * (x + 1) * x + 2 * (x + 1) * (x - 0.5) * x


def ff_x(x):
    return ((3 * x ** 2 - 1) / (3 * x ** 2 + 2)) ** (8 * x ** 2)


x = np.linspace(0, 10000000000, 500000)
y = ((3 * x ** 2 - 1) / (3 * x ** 2 + 2)) ** (8 * x ** 2)
print(f'Значение предела в 100000 {ff_x(1000000)}')
print(f'Значение предела в 1000000000000 {ff_x(1000000000)}')
print(f'e^-8 {np.e**-8}')


plt.plot(x, y)
plt.plot(np.e**-8, np.e**-8)
plt.show()
