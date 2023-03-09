# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic (n,a,d) :
    array = []
    array.append(a)
    j = 2
    i = 1 
    for i in range(n):
        array.append(first_element + (j-1) * d)
        j+=1
    return (print (array))

print("Введите количество элементов массива :")
quantity = int(input())
print("Введите первый элемент :")
first_element= int(input())
print("Введите разность :")
d = int(input())
arithmetic (quantity,first_element,d )
