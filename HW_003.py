# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

list = []
for i in range(random.randint(5,7)):
    list.append(random.randint(1,10))
print(list)

sum = 0
for i in range(1,len(list), 2):
    sum += list[i]
print(f'Сумма нечетеных элементов: {sum}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import random

# list = []
# for i in range(random.randint(5,7)):
#     list.append(random.randint(1,10))
# print(list)

# newList = []
# ind = -1

# if len(list)%2 == 0:
#     lenght = len(list)//2
# else:
#     lenght = len(list)//2 + 1
# for i in list[:lenght]:
#     newList.append(i * list[ind])
#     ind -= 1
# print(newList)

# 3. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# a = [1.1, 1.2, 3.1, 5, 10.01, 4]
# b=[]
# for i in a:
#     b.append(round(i - round(i,0),2))
# for i in b:
#     if i == 0:
#         b.remove(i)
# print(a)
# print(b)
# max = b[0]
# min = b[1]
# for i in b:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print (max - min)

# 4. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('Десятичное число: '))
# result = ''
# while num > 0:
#    result = str(num % 2) + result
#    num //= 2
# print(int(result))

# 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# num = int(input('Число: '))
# a = [0,1]
# i = 2
# while i <= num:
#     a.append(a[i-2]+a[i-1])
#     i += 1
# b = [1,0]
# i=0
# while i >= -num + 2:
#     b.insert(0, b[i-1]-b[i-2])
#     i -=1
# b.remove(0)
# print(b + a)
