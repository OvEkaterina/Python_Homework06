# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
list= []
print("Введите количество эллментов массива :")
n = int(input())
from random import randint
for i in range(n):
   list.append(randint(1, n)) 
print(list)
print("Введите значение х :")
x = int(input())
list_new =[abs(x-i) for i in list]
print(list[list_new.index(min(list_new))])

