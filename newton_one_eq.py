import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Eq must have second derivative; First and second derivatives must not change sign at the interval;
# So we can find one root in the [a, b] interval.

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
x = .5
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
d_first = {'num iter': hist[0], 'x': hist[1], 'f(x)': hist[2]}
# will print history of iterations
print(pd.DataFrame(data=d_first).to_string(index=False))


# principle of the algorithm on another, more convex function:

def view(x):
    return 0.005 * np.e ** x - 1


def derivative_view(x):
    return 0.005 * np.e ** x


def tangent(a, f_x, derivative, xa):
    return f_x(a) + derivative(a) * (xa - a)


hist_sec = optimize(view, derivative_view, 10)
d_second = {'num iter': hist_sec[0], 'x': hist_sec[1], 'f(x)': hist_sec[2]}
print(pd.DataFrame(data=d_second).to_string(index=False))

xa = np.linspace(4.5, 6.75, 30)
xxa = np.linspace(4.5, 6.75, 30)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(4.5, 6.75)
ax.plot(xa, view(xa))
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')


def plot_tangent(f_x, derivative, x_ax, num_iter, hist):
    """
    :param f_x: function to that tangent line will be plotted
    :param derivative: derivative of above function
    :param x_ax: ndarray for plotting
    :param num_iter: sets iteration for which tangent line will be plotted
    Function will plot line on the active axes
    """
    tangent_line = tangent(hist[1][num_iter], view, derivative, x_ax)
    ax.plot(x_ax[np.where(tangent_line > 0)], (tangent_line[np.where(tangent_line > 0)]))
    x_next = -f_x(hist[1][num_iter]) / derivative(hist[1][num_iter]) + hist[1][num_iter]
    # dot on Ox
    ax.scatter(x_next, 0, marker='x', color='r', s=45, label=f'X for {num_iter + 1} iter')
    ax.legend()
    # Function value in above dot. X_k+1 for iteration process.
    ax.vlines(x_next, ymax=view(x_next), ymin=0, linestyle='--')


plot_tangent(view, derivative_view, xxa, 3, hist_sec)
plot_tangent(view, derivative_view, xxa, 4, hist_sec)
plt.show()
