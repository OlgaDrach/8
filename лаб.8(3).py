#3)виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
#Результати множення елементів занесіть до нової матриці та виведіть #її на екран.

import random
import numpy
#робимо 2 масива з нулів(тип цілих чисел)
g = numpy.zeros((3,3),dtype = int)
for z in range(3):
    for x in range(3):
        g[z,x]=random.randint(-10,10)
# виводимо першу матрицю
print('Перша матриця:   \n', g)
v = numpy.zeros((3,3),dtype = int)
for k in range(3):
    for l in range(3):
        v[k,l]=random.randint(-10,10)
#спочатку створюємо масив з нулів для роботи з ним
t = numpy.zeros((3,3),dtype = int)
# виводимо другу матрицю
print('Друга матриця:  \n', v)
#через цикл перемножуємо по елементно
for z in range(3):
    for x in range(3):      
        t[z,x] = g[z,x] * v[z,x]
#виводимо перемножиену матрицю
print('Перемножені матриці:  \n', t)
