import numpy as np
import matplotlib.pyplot as plt

y = np.arange(-3, 3, 0.05)
x = np.arange(-3, 3, 0.05)
x = y ** 2
x_2 = -y/3 - 2/3
plt.plot(np.arange(-3, 3, 0.05), x)
plt.plot(np.arange(-3, 3, 0.05), x_2)
plt.grid('True')
plt.show()