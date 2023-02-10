'''import numpy as np
x = np.array([[-1.], [-1.]])
#J = ((2 * x[0][0] * 3 * x[1][0] ** 2 - 2 * x[1][0] * np.e ** (x[0][0] - 1)) ** - 1) * (np.array([[3 * x[1][0] ** 2, - np.e ** (x[0][0] - 1)], [-2 * x[1][0], 2 * x[0][0]]]))
J = np.array([[0.40809227, -0.0560692], [-0.13603076, 0.10202307]])
delta = float(1.)
cnt = int(0)
print(J)
while delta > 0.001:
    cnt += 1
    x_hist = x
    F = np.array([[x_hist[0][0] ** 2 + x_hist[1][0] ** 2 - 2], [np.e ** (x_hist[0][0] - 1) + x_hist[1][0] ** 3 - 2]])
    x = x - J.dot(F)
    delta = abs(max(abs(x_hist) - abs(x)))
    print(f'Iter = {cnt}, x_1 = {x[0][0]}, x_2 = {x[1][0]}, delta ={delta}')'''
import numpy as np
x = np.array([[-1.], [-1.]])
#J = ((2 * x[0][0] * 3 * x[1][0] ** 2 - 2 * x[1][0] * np.e ** (x[0][0] - 1)) ** - 1) * (np.array([[3 * x[1][0] ** 2, - np.e ** (x[0][0] - 1)], [-2 * x[1][0], 2 * x[0][0]]]))
J = np.array([[0.40809227, -0.0560692], [-0.13603076, 0.10202307]])
delta = float(1.)
cnt = int(0)
print(J)
while delta > 0.001:
    cnt += 1
    x_hist = x
    F = np.array([[x_hist[0][0] ** 2 + x_hist[1][0] ** 2 - 2], [np.e ** (x_hist[0][0] - 1) + x_hist[1][0] ** 3 - 2]])
    x = x - J.dot(F)
    delta = (max(abs(x_hist - x)))
    print(f'Iter = {cnt}, x_1 = {x[0][0]}, x_2 = {x[1][0]}, delta ={delta}')