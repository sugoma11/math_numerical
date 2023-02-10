from numpy import array


def read_matrix():
    matrix = []
    print('Enter number of rows: ')
    i = float(input())
    print('Enter matrix: ')
    if not i.is_integer():
        raise ValueError('N rows not int!')
    for k in range(int(i)):
        matrix.append(list(map(float, input().split())))
        if len(matrix[k]) != len(matrix[k - 1]) or len(matrix[k]) != i + 1:
            raise ValueError('Matrix size error')
    matrix = array(matrix)
    return matrix[:, :-1], matrix[:, -1]


def reg(A, b):
    return A.T.dot(A), A.T.dot(b)