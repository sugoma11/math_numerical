import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x**2 + y**2


x_val_adv = []
y_val_adv = []
h_adv = float(0.2)
x_adv = int(0)
y_prev_adv = float(0.5)
y_next_adv = float(0.0)
while 1:
    x_val_adv.append(x_adv)
    y_val_adv.append(y_prev_adv)
    y_next_adv = y_prev_adv + h_adv * f(x_adv + 0.5 * h_adv, y_prev_adv + 0.5 * h_adv * f(x_adv, y_prev_adv))
    print(f'x = {x_adv} y_next = {y_next_adv}')
    x_adv += h_adv
    print(f'y_prev = {y_prev_adv}')
    y_prev_adv = y_next_adv
    if x_adv == 1.2:
        break

plt.plot(x_val_adv, y_val_adv, c='r')
plt.show()