# Найти НОК двух чисел: наимаеньшее число, которое делится на оба числа
# Разложить на простые множители, отметить все одинаковые множители. 
# из большего числа все перемножаем, а из меньшего несовпадения

number1 = int(input('введите первое число => '))
number2 = int(input('введите второе число => '))

i = min(number1, number2)
while True:
    if i % number1 == 0 and i % number2 == 0:
        break
    i += 1
print(i)



#Вычислить число Пи c заданной точностью d / пи = c/d
#Пример: при d = 0.001,  c= 3.141

# Формула Бэйли — Боруэйна — Плаффа
import math
from math import pi

n = pi
print(n)
n = 100
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

print(round((my_pi), 3))


# 3 Составить список простых множителей натурального числа N

number = int(input('введите натуральное число => '))
if number > 0:
    print('натуральное, будем искать множители')
elif number == 1:
    print('делитель только 1')
else:
    print("Давайте другое число")
i=1

list = []
while True:
    if number % i == 0:
        list.append(i)
    i += 1
print(list())

#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

from random import randint

def new_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = new_list(size, m, n)
print(origin)
print(unic_value(origin))

# + на тему файловой системы:
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

with open('file.txt', 'a') as data:
   data.write('\n2\n')
   data.write('3\n')
   data.write('4\n')
   data.write('5\n')
   data.close()

Дальше не получается


