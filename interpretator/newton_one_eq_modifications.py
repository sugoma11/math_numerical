import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Eq must have second derivative;
# In simple Newton method we calculate derivative only once;
# So we can find one root in the [a, b] interval.

# to hide exp form
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# eq to solve and it's derivative:
def f_x(x):
    return x ** 3 - x ** 2 + x + 2


def derivative_f(x):
    return 3 * x ** 2 - 2 * x + 1


def tangent(a, f_x, derivative, xa, simple=False, x_0=None):
    """
    :param a: float; define dot, where we plot line
    :param f_x: function; function for what we plot line
    :param derivative: function; derivative of f_x
    :param xa: ndarray; arg of f_x
    :param simple: bool; flag for simple method
    :param x_0: float; point from where iteration process was started
    :return: ndarray; tangent line in point a
    """
    if simple:
        return f_x(a) + derivative(x_0) * (xa - a)
    else:
        return f_x(a) + derivative(a) * (xa - a)


def plot_tangent(f_x, derivative, x_ax, num_iter, hist, simple=False):
    """
    :param f_x: function to that tangent line will be plotted
    :param derivative: derivative of above function
    :param x_ax: ndarray for plotting
    :param num_iter: sets iteration for which tangent line will be plotted
    Function will plot line on the active axes
    """
    if simple:
        # using tangent angle from first point
        tangent_line = tangent(hist[1][num_iter], f_x, derivative, x_ax, simple=True, x_0=hist[1][0])
        ax.plot(x_ax[np.where(tangent_line > 0)], (tangent_line[np.where(tangent_line > 0)]))
        x_next = -f_x(hist[1][num_iter]) / derivative(hist[1][0]) + hist[1][num_iter]
    else:
        tangent_line = tangent(hist[1][num_iter], f_x, derivative, x_ax)
        ax.plot(x_ax[np.where(tangent_line > 0)], (tangent_line[np.where(tangent_line > 0)]))
        x_next = -f_x(hist[1][num_iter]) / derivative(hist[1][num_iter]) + hist[1][num_iter]
    # dot on Ox
    ax.scatter(x_next, 0, marker='x', s=45, label=f'X for {num_iter + 1} iter')
    ax.legend()
    # Function value in above dot. X_k+1 for iteration process.
    ax.vlines(x_next, ymax=f_x(x_next), ymin=0, linestyle='--')


# eq graphic:
xa = np.linspace(-2, 2, 50)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xa, f_x(xa))
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')


'''
Here is difference between methods: we calculate derivative only in the start point, so method has
linear convergence;
c - parameter of convergence speed from Newton-Broyden method. If convergence is bad,
c must be in [0, 1], else it may be > 1;
'''

def optimize(f_x, derivative_f, x, delta=0.0001, c=1, simple=False):

    cnt = 0
    x_next = 0
    hist = [[] for i in range(3)]
    df_dx = derivative_f(x)

    while 1:
        if simple:
            x_next = x - c * (f_x(x) / df_dx)
        else:
            x_next = x - c * (f_x(x) / derivative_f(x))

        x = x_next

        hist[0].append(cnt)
        hist[1].append(x)
        hist[2].append(f_x(x))

        cnt += 1
        if cnt > 2:
            if abs(hist[2][cnt - 2] - f_x(x)) < delta:
                break

    return hist


hist = optimize(f_x, derivative_f, 3., simple=True)
d_first = {'num iter': hist[0], 'x': hist[1], 'f(x)': hist[2]}
# will print history of iterations
print(pd.DataFrame(data=d_first).to_string(index=False))

# all tangent lines must be parallel to first
for i in range(len(hist[0])):
    if i % 20 == 0:
        plot_tangent(f_x, derivative_f, xa, i, hist, simple=True)
plt.show()