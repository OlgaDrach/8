#Пошук підрядка

s = 'Справа был установлен ряд киноаппаратов, чтобы запечатлеть на ленте все моменты выступления Керна о оживление головы, а на эстраде разместился почетный президиум из наиболее крупных представителей ученого мира.'
print(s)
#Підрядка не буде знайдена, якщо її не буде в рядку, тоді виведе що підрядок не знайдено
s1=input('Введіть підрядок ')
#індекси рядки
i=-1 
#Індексі подстроки
o=0
while (o<len(s1)) and i<(len(s)-len(s1)):
    o=0
#Кількість зсувів, і одночасно наша позиція
    i+=1 
    while o<len (s1) and s1[o]==s[i+o]:
        o+=1
if (o==len(s1)):
    print(f'Підрядок знайдений в позиції {i},за {i} переміщень')
else:
    print('Підрядок не знайдений')
