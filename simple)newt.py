import numpy as np
import time


def f_x(x):
    return (1 - np.cos(x)) ** 0.5 - 1 + 0.2 * x


def f_dx(x):
    return np.sin(x) / (2 * (1 - np.cos(x)) ** 0.5) + 0.2


x = 1.


while 1:
    x = x - f_x(x) / f_dx(x)
    print(x, f_x(x))
    time.sleep(1)