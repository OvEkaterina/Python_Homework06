# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def array_random(n, min, max):
    list = []
    from random import randint
    for i in range(n):
        list.append(randint(min, max)) 
    return(list)

print("Введите количество элементов массива :")
n = int(input())
print("Введите минимальное значение элемента массива :")
min_array = int(input())
print("Введите максимальное значение элемента массива :")
max_array = int(input())

arr = array_random(n, min_array, max_array)
print (arr)
print("Введите минимальное значение диапазона :")
min = int(input())
print("Введите максимальное значение диапазона :")
max = int(input())
for i in range (len(arr)) :
    if  arr[i] <= max and arr[i] >= min :
     print (i , end = " ")