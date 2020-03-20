#виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
#користувачем).

import numpy as np
h,l = int(input('Ввести h:')), int(input('Ввести l:'))
v = np.zeros((h,l),dtype = int)
e = np.zeros((h,l),dtype = int)
for i in range(h):
    for j in range(l):
        v[i,j] = int(input(f'A[{i},{j}]= '))
print(v)
for i in range(h):
    for j in range(l):
        if i != j:
            e[i][j] = v[j][i]
        else:
            e[i][j] = v[i][j]
print(f'Транспортована матриця: \n{e}')
