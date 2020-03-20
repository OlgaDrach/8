#   1 2. Задача полягає у вивченні і реалізації алгоритмів пошуку для #даних, підготовлених
#за допомогою функції моделювання випадкових чисел і текстів, #підготовлених самостійно.
#   Для кожного алгоритму необхідно підготувати тести, що підтверджують працездатність програми. Для всіх алгоритмів пошуку повинні бути #приведені лістинги програм пошуку та лістинги результатів (номера позиції в вихідному #масиві, починаючи
#з якого розташований елемент або фрагмент пошуку; кількості порівнянь по кожному алгоритму пошуку).


#Лінійний пошук

import numpy as np
import random
#Створимо масив, для перевірки правильності пошуку.
b1 = np.array(range(1,10))  
print(b1)
#Якщо користувач введе більше 9, то елемент знайдений не буде
g = int(input('Введіть елемент для пошуку '))
k = len(b1)
 #Введемо лічильник для підрахунку кількості ітерацій і перебору нашого масиву
count = 0                           
#Вводимо лінійний пошук
while count < k and b1[count] != g:  
    count += 1
#кількість порівнянь, починається з 0 з кроком 1 значення в нашому завданні необхідно х-1 кроків
print('Кількість порівнянь ',count)  
if count == k:
    print('Елемент не знайдений ')
else:
    print(f'На позиції {count} знайдений {g}')
#Робота програми з рандомними значеннями
b2 = np.zeros(20,dtype=int)
for i in range(20):
    b2[i] = random.randint(-10,10)
print(b2)
k1 = len(b2)
count2 = 0
#Вводимо лінійний пошук
while count2 < k and b2[count2] != g:  
    count2 += 1
#кількість порівнянь
print('Кількість порівнянь',count2)  
if count2 == k1:
    print('Елемент не знайдений')
else:
    print(f'На позиції {count2} знайдений {g}')
