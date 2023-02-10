import numpy as np


def f(x):
    return (np.sqrt(2 * x + np.e ** x)) ** -1


sum = float(0.0)
for i in range(10000):
    gamma = np.random.rand(1, 1)[0][0]
    ksi = 3 / 2 * gamma
    sum += f(ksi) * (3 / 2)
print(sum / 10000)
