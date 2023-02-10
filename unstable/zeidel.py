import numpy as np
import time


def get_cube_root(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root


def f(x):
    return get_cube_root((-x-5) / 3)


def F(x):
    return 3 * x ** 3 + x + 5


x = float(-1.5)
x_k1 = float(0.0)
cnt = int(0)
while 1:
    x_k1 = f(x)
    x = x_k1
    print(f'Iter = {cnt}, x = {x}, f(x) = {F(x)}')
    cnt += 1
    time.sleep(1)