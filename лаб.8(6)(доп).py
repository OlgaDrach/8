#Бінарий пошук

import numpy as np
import random
#Створимо масив, для перевірки пошуку.
k1 = np.array(range(1,16))  
print(k1)
#якщо ввести більше 15, то елемент знайдений не буде
t = int(input('Введіть елемент для пошуку '))
#Конець масиву
P = len(k1)-1 
#Початок масиву, лічильник для порівнянь,змінна для позиції числа
E, count, k = 0,0,0, 
flag = False
while E <= P and not flag :
#якщо ввести 9, При першій ітерації, к = 6, при другій к = 10 при третин к = 8
    r = (E + P)//2 
#лічильник ітерацій
    count += 1   
    if k1[k] == t:
        flag = True
    elif k1[r] < t:
        E = r+1
    else:
        P = r-1
if not flag:
    print('Елемент не знайдено')
else:
    print(f'Елемент знайдений на позиції {r} за {count} порівнянь')
#Робота з рандомними значеннями
k2 = np.zeros(20, dtype = int)
for i in range(20):
    k2[i] = random.randint(-10,10)
print(k2)
#Кінець масиву
P1 = len(k2)-1 
#Початок масиву, лічильник для порівнянь, змінна для позиції числа
E1,count1,r1 = 0,0,0, 
flag1 = False
while E1 <= P1 and not flag1 :
    r1  (E1 + P1)//2
#лічильник ітерацій
    count1 += 1   
    if k2[k1] == t:
        flag1 = True
    elif k2[r1] < t:
        E1 = k1+1
    else:
        P1 = k1-1
if not flag1:
    print('Елемент не занйдений')
else:
    print(f'Елемент знайдений на позиції {k1} за {count1} порівнянь')
