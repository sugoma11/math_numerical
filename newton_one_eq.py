import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# to hide exp form
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# eq to solve and it's derivative:

def f_x(x):
    return x ** 3 - x ** 2 + x + 2


def derivative_f(x):
    return 3 * x ** 2 - 2 * x + 1


# eq graphic:
x = np.linspace(-2, 2, 30)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, f_x(x))
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.show()


cnt = 0
x = -5.
x_fut = 0
delta = 0.0001
hist = [[] for i in range(3)]

while 1:
    x_fut = x - f_x(x) / derivative_f(x)
    x = x_fut

    hist[0].append(cnt)
    hist[1].append(x)
    hist[2].append(f_x(x))

    cnt += 1
    if cnt > 1:
        if abs(hist[1][cnt - 2] - x) < delta:
            break


d = {'num iter': hist[0], 'x': hist[1], 'f(x)': hist[2]}

print(pd.DataFrame(data=d).to_string(index=False))
