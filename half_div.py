import numpy as np
import time

a = float(-1.)
b = float(-0.5)
cnt = int(0)
c = 0.


def get_cube_root(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root


def f_x(x):
    return get_cube_root(x ** 3 - x ** 2 + x + 2)


while 1:
    if f_x(a) * f_x(c) < 0:
        b = (a + b) / 2
    elif f_x(b) * f_x(c) < 0:
        a = (a + b) / 2
    c = (a + b) / 2
    if (b - a) / 2 < 0.001:
        break

    print(cnt)
    print(f'a = {a}; f(a) = {f_x(a)}; b = {b}; f(b) = {f_x(b)}; c = {(a + b) / 2}; f(c) = {f_x(c)}; delta = {0.5 * (b - a)}')
    cnt += 1