import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

# equation to solve: x ** 3 = ln(x + 1)
# x ** 3 - ln(x + 1) = 0
# evident that it one of roots is x = 0; let's see graph


def f_x(x):
    return x ** 3 - np.log(x + 1)


x = np.arange(-1, 1.5, 0.075)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, f_x(x))
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.show()

# so initialize a == 0.5, b == 1.0
#
a = float(.5)
b = float(1.)
cnt = int(0)
c = (a + b) / 2
epsilon = 0.0001

a_hist = []
b_hist = []
c_hist = []

while b - a > 2 * epsilon:

    if f_x(a) * f_x(c) < 0:
        b = (a + b) / 2

    elif f_x(b) * f_x(c) < 0:
        a = (a + b) / 2

    b_hist.append(b)
    a_hist.append(a)
    c = (a + b) / 2
    c_hist.append(c)
    cnt += 1

d = {'num iter': [i for i in range(cnt)], 'a': a_hist, 'b': b_hist, 'F(a)': map(f_x, a_hist),
     'F(b)': map(f_x, b_hist), 'c': c_hist, 'F(c)': map(f_x, c_hist),
     'b - a / 2': ((np.asarray(b_hist) - np.asarray(a_hist)) / 2)}

print(pd.DataFrame(data=d))
