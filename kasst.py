import numpy as np
import matplotlib.pyplot as plt
import time


def f_x(x):
    return x ** 3 - x ** 2 + x + 2


x_arr = np.array([0.1])
cnt = 0
x = -1.

while 1:
    x_fut = x - (x - x_arr[cnt]) / (1 - f_x(x_arr[cnt]) / f_x(x_arr[cnt]))
    x = x_fut
    x_arr = np.hstack((x_arr, x))
    print(x_arr)
    print(f'iter = {cnt}, x = {x}, f_x = {f_x(x)}')
    cnt += 1
    time.sleep(1)
