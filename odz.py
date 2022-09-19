import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-1, 4, 0.05)
y = np.arange(-1, 4, 0.05)
x_ax, y_ax = np.meshgrid(x, y)
tst_x = 2
tst_y = 1
tstax1, tstax2 = np.meshgrid(tst_x, tst_x)
vals = np.zeros((len(x), len(y)))
for k in range(len(x)):
    for l in range(len(y)):
        #assemble_temp = np.array([[x[k]], [y[l]]])
        vals[k][l] = (x[k]-1)**3 + (y[l]-2)**2 - 3 * x[k]
        #print(vals[k][l])
fig = plt.figure()
ax_3d = fig.add_subplot(111, projection='3d')
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
ax_3d.plot_surface(x_ax, y_ax, np.transpose(vals), cmap='inferno')
ax_3d.scatter(tstax1, tstax2, 0, s=5, color='g')
plt.show()
