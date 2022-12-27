#1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# num = (input('Введите вещественное число: '))
# if '.' in num:
#     num = [str(i) for i in num]
#     num.remove('.') 
# num1 = [int(i) for i in num]
# print(f'Сумма цифр: {sum(num1)}')

# Вариант преподавателя

# s = '0.56'
# summ = 0
# for i in s:
#     if i.isdigit(): # проверка является ли символ в строке цифрой
#         summ += int(i) # если итый символ цифра он суммируется к сумме
# print(summ)

#2. Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.

# n = int(input('Число: '))
# i = 2
# list = [1]
# fact = 1
# while i <= n:
#     fact *= i 
#     list.append(fact)
#     i += 1
# print(list)

#3. Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.

# num = int(input('Число: ')) 
# dict = {} 
# summa = 0
# for i in range(1,num+1): 
#     dict[i] = round((1 + 1/i)**i, 2)
#     summa += dict[i]
# print(dict) 
# print(summa)

#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random 
# num = int(input('Количество элементов: ')) 
 
# def NewRandomArray(num):
#     list=[]
#     for i in range(random.randint(num,num)): 
#         list.append(random.randint(-num, num))
#     return list
# list1 = NewRandomArray(num)
# print(list1)

# multy = 1
# data = open('file.txt', 'r') 
# a = data.readlines()
# print('Элементы:')

# for i in a:
#     ind = int(i.strip())
#     print(f'[{ind}] {list1[ind]}') 
#     multy = multy * list1[ind]
# print(f'Произведение элементов = {multy}')   

# data.close() 

# Вариант преподавателя
result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
result *= numbers[int(line)]
f.close()
print(result)

#Реализуйте алгоритм перемешивания списка.

#Вариант 1 - рандомное перемешивание

# import random

# def NewRandomArray():
#     list=[]
#     for i in range(random.randint(5,7)): 
#         list.append(random.randint(1,10)) 
#     print(list)
#     return list
# a = NewRandomArray()
# random.shuffle(a)
# print(a)

#Вариант 2 - пузырьковая сортировка

# from random import randint
 
# n = 6
# a = []
# for i in range(n):
#     a.append(randint(1, 10))
# print(f'Исходный массив: {a}')
 
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
 
# print(f'Итоговый массив: {a}')
