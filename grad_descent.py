import numpy as np
import time

def f_x(x):
    return (x[0][0]-1)**3 + (x[1][0]-2)**2 - 3 * x[0][0]


def dx(x):
    x[0][0] = 3 * x[0][0] ** 2 - 6 * x[0][0] - 2 * x[1][0]
    x[1][0] = 2 * x[1][0] - 2 * x[0][0]
    return x


x = np.array([[2], [1]])
while 1:
    x = x - 0.25 * dx(x)
    print(f'x = {x} f(x) = {f_x(x)}')
    time.sleep(3)

