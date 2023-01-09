import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# to hide exp form
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# eq to solve and it's derivative:
def f_x(x):
    return x ** 3 - x ** 2 + x + 2


def derivative_f(x):
    return 3 * x ** 2 - 2 * x + 1


# eq graphic:
xa = np.linspace(-2, 2, 30)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xa, f_x(xa))
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.show()

# initialize start approximation and precision:
x = -5.
delta = 0.001


def optimize(f_x, derivative_f, x, delta=0.0001):

    cnt = 0
    x_next = 0
    hist = [[] for i in range(3)]

    while 1:
        x_next = x - f_x(x) / derivative_f(x)
        x = x_next

        hist[0].append(cnt)
        hist[1].append(x)
        hist[2].append(f_x(x))

        cnt += 1
        if cnt > 2:
            if abs(hist[2][cnt - 2] - f_x(x)) < delta:
                break

    return hist


hist = optimize(f_x, derivative_f, x, delta)
d = {'num iter': hist[0], 'x': hist[1], 'f(x)': hist[2]}
# print(pd.DataFrame(data=d).to_string(index=False))


# principle of the algorithm on another, more convex function:

def view(x):
    return 0.005 * np.e ** x - 1


def derivative_view(x):
    return 0.005 * np.e ** x


def tangent(a, f_x, derivative, xa):
    return f_x(a) + derivative(a) * (xa - a)


hist = optimize(view, derivative_view, 10)
d = {'num iter': hist[0], 'x': hist[1], 'f(x)': hist[2]}
print(pd.DataFrame(data=d).to_string(index=False))

xa = np.linspace(4.5, 6.75, 30)
xxa = np.linspace(4.6, 6.75, 60)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(5, 6.75)
ax.plot(xa, view(xa))

tangent_line_one = tangent(hist[1][3], view, derivative_view, xxa)
ax.plot(xxa[np.where(tangent_line_one > 0)], (tangent_line_one[np.where(tangent_line_one > 0)]))

x_next = -view(hist[1][3]) / derivative_view(hist[1][3]) + hist[1][3]
ax.scatter(x_next, 0, marker='x', color='r', s=100)
ax.vlines(x_next, ymax=view(x_next), ymin=0, linestyle='--')

tangent_line_two = tangent(hist[1][4], view, derivative_view, xxa)
ax.plot(xxa[np.where(tangent_line_two > 0)], (tangent_line_two[np.where(tangent_line_two > 0)]))

x_next = -view(hist[1][4]) / derivative_view(hist[1][4]) + hist[1][4]
ax.scatter(x_next, 0, marker='x', color='r', s=50)
ax.vlines(x_next, ymax=view(x_next), ymin=0, linestyle='--')

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.show()
