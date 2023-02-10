import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 4, 0.25)
y = np.arange(-1, 4, 0.25)

x, y = np.meshgrid(x, y)

# define coords of dot
dot_x = 2
dot_y = 1
dot_z = 3

# define z = f(x, y) function
def z(x, y):
    return (x - 1) ** 3 + (y - 2) ** 2 - 3 * x


fig = plt.figure()
ax_3d = fig.add_subplot(111, projection='3d')
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
# z = f(x, y) surface
ax_3d.plot_wireframe(x, y, z(x, y), alpha=0.75)
# add dot to graphic
ax_3d.scatter(dot_x, dot_y, dot_z, s=50, color='r', marker='x')
plt.show()
