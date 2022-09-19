import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (np.sqrt(2 * x + np.e ** x)) ** -1


x = 1.5 * np.random.rand(1, 10000)
E_x = f(x)
y_bigger = []
x_bigger = []
x_small = []
y_small = []

cnt = int(0)
for i in range(10000):
    x = 1.5 * np.random.rand(1, 1)[0][0]
    y = np.random.rand(1, 1)[0][0]
    if f(x) > y:
        cnt += 1
        x_small.append(x)
        y_small.append(y)

    else:
        y_bigger.append(y)
        x_bigger.append(x)

print(cnt/10000 * 1.5)


plt.scatter(x_small, y_small, c='red', linewidths=1, marker='x')
plt.scatter(x_bigger, y_bigger, c='green', linewidths=0.25, marker='^')
plt.plot(np.linspace(0, 1.5, 10000), f(np.linspace(0, 1.5, 10000)))
plt.show()
