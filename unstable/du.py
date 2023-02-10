import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x**2 + y**2


def fxy(x, y):
    return y * x ** 2 + y ** 3 / 3

ox = np.linspace(0, 3)
oy = np.linspace(0, 3)
vals = np.zeros((len(ox), len(oy)))
os_x, os_y = np.meshgrid(ox, oy)

x_val = []
y_val = []
h = float(0.2)
x = int(0)
y_prev = float(0.5)
y_next = float(0.0)
while 1:
    x_val.append(x)
    y_val.append(y_prev)
    y_next = y_prev + h * f(x, y_prev)
    print(f'x = {x} y_next = {y_next}')
    x += h
    print(f'y_prev = {y_prev}')
    y_prev = y_next
    if x == 1.2:
        break

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
for i in range(len(ox)):
    for j in range(len(oy)):
        vals[i][j] = fxy(ox[i], oy[j])


fig = plt.figure()
ax_3d = fig.add_subplot(111, projection='3d')
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
ax_3d.plot_surface(os_x, os_y, np.transpose(vals), cmap='autumn')
plt.plot(x_val_adv, y_val_adv, c='r')
plt.plot(x_val, y_val, c='g')
plt.show()

