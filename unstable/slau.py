import numpy as np
from normalize import read_matrix, reg
import time
A, b = read_matrix()
A, b = reg(A, b)

x = []
for k in range(len(A)):
    x.append(A[k][k])
c = x.copy()
while 1:
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                if c[i] > 0 and A[i][j] > 0 or c[i] < 0 and A[i][j] < 0:
                    x[i] += A[i][j] / c[i]

                elif ((c[i] > 0) and (A[i][j] < 0)) or ((c[i] < 0) and (A[i][j] > 0)):
                    x[i] += -A[i][j] / c[i]

        if c[i] > 0 and b[i] > 0 or c[i] < 0 and b[i] < 0:
            x[i] -= b[i] / c[i]

        elif ((c[i] > 0) and (b[i] < 0)) or ((c[i] < 0) and (b[i] > 0)):
            x[i] += b[i] / c[i]

    print(x)
    time.sleep(1)