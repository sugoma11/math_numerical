import numpy as np
import time

cnt = int(0)
x_2 = float(2.)
x_3 = float(1.)
while 1:
    x_1 = 0.5 * x_2 + 1/6 * x_3 + 1/3
    x_2 = x_3 * 0.5 + 1 / 2
    x_3 = 0.5 * x_1 - 0.25 * x_2 + 0.75
    cnt += 1
    print(f'Iter = {cnt}, x_1 = {x_1}, x_2 = {x_2} x_3 = {x_3}')
