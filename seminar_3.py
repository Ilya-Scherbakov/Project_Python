# # ФУНКЦИИ

# def hello(): # чтобы задать функцию пиши def. В скобках писать аргументы кот фун. может принимать. их может и не быть(в данном случае)
#     print('hello') # эта фун. выполняет принт на экран

# hello() # так вызывается функция

# # -------------------

# def hello(name): # тут задали аргумент имя, и будет выводить hello Илья
#     print('hello', name)

# hello('Илья')

# # -------------------

# def hello(name='незнакомец'): # тут задали аргумент имя, и будет выводить hello Илья
#     print('hello', name)

# hello() # теперь если тут не напишем имя, он выведет незнакомец. Если напишем, то выведем имя

# # -------------------

# def mult(a=1, b=3):
#     return a*b # пишем ретурн если хотим этот результат записать в след переменную, иначе не запишется

# m = mult(5, 2)
# print(m)

# -------------------------------
# Задача 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайный чисел

# # ХУЙ ЗНАЕТ КАК ОН РЕШИЛ, ЭТО ПИПЕЦ
# import time
# print(time.time())
# some_list = [1, 7, 8, 12]
# for _ in range(int(str(time.time()).split('.')[1]) % (10 - 5 + 1) + 5):
#     i1 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
#     time.sleep(0.0001)      # единственное что понятно это притормозить работу этой функцией
#     i2 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
#     some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
# print(some_list)

# -------------------------------
# Задача 20. Задайте список. Программа, которая определит присутствует ли в заданном списке строк некое число

# a = []
# n = int(input('Введи кол-во строк: '))
# for i in range(n):
#     a.append(input('теперь вводи их столько раз: '))
# # a = [input() for _ in range(int(input()))] # сокращенная запись создания списка(предыдущих 4х строк)
# find_number = input('введите что будешь искать: ')                        # искомое число(то что будем искать)
# if find_number in a:
#     print('да')
# else:
#     print('нет')

# втрой вариант с поиском элемента в строке(более куртое решение)
# a = []
# n = int(input('Введи кол-во строк: '))
# for i in range(n):
#     a.append(input('теперь вводи их столько раз: '))
# find_number = input('введите что будешь искать: ')
# for i in a:
#     if find_number in i:
#         print('да')
#         break
#     else:
#         print('нет')

# -------------------------------
# Задача 21. Программа, которая определит позицию второго вхождения строки в списке либо сообщит что ее нет

# a = []
# n = int(input())
# for i in range(n):
#     a.append(input())
# find_str = input()
# count = 0
# for el in range(len(a)):
#     if a[el] == find_str:
#         count += 1
#     if count == 2:
#         print(el)
#         break
# else:
#     print(-1)

# второй метод
# # хуйзнат как решил
# a = []
# n = int(input())
# for i in range(n):
#     a.append(input())
# find_str = input()
# first = a.index(find_str) # метод индекс ищет первое вхождение
# second = a.index(find_str, first) # тут чето продолжит со след индекса искать
# print(second)

# Задача 22 (ДЗ). Задайте список из нескольких чисел. Программа, кот найдёт сумму эл-ов списка, стоящих на нечётной позиции.

from random import *

# n = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(n):
#     some_list.append(randint(-12, 15))
# summ = 0
# for i in range(1, len(some_list), 2):
#         summ += some_list[i]
# print(f"{some_list} -> сумма элементов на нечётных позициях: {summ}")

# Решал преподаватель

# count = int(input('введите кол-во элементов: '))
# some_list = []
# summa = 0
# for _ in range(count):          # тут ввод руками списка
#     number = int(input())
#     some_list.append(number)

# for idx in range(1, count, 2):
#     summa += some_list[idx]
# print(summa)

# Задача 23 (ДЗ). Программа, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# n = int(input('Введите кол-во элементов: '))
# some_list = []
# res_list = []
# summ = 0
# for _ in range(n):
#     some_list.append(randint(-12, 15))
# for i in range(len(some_list) // 2 + (len(some_list) % 2)):
#     summ = int(some_list[i] * (some_list[len(some_list) - 1 - i]))
#     res_list.append(summ)

# Решал преподаватель

# count = int(input('введите кол-во элементов: '))
# some_list = []
# for _ in range(count):          # тут ввод руками списка
#     number = int(input())
#     some_list.append(number)
# new_list = []
# for idx in range((count - 1) // 2 + 1):
#     number1 = some_list[idx]
#     number2 = some_list[count - idx - 1]
#     new_list.append(number1 * number2)
# print(new_list)

#  Задача 24 (ДЗ). Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# from random import uniform

# def list_rand_nums(count):
#     list_nums = []
#     for i in range(count):
#         list_nums.append(round(uniform(1, count), 2))
#     return list_nums


# def dif_min_max(list_nums):
#     num_max = list_nums[0] % 1
#     num_min = list_nums[0] % 1
#     for i in range(1, len(list_nums)):
#         num = round(list_nums[i] % 1, 2)
#         if num > num_max:
#             num_max = num
#         elif num < num_min:
#             num_min = num

#     result = round(num_max - num_min, 2)
#     # print(f'мин знач {num_min}, макс: {num_max}, разница: {result}')
#     return result

# complite = list_rand_nums(int(input("введите кол-во строк: ")))
# print(complite)
# print(dif_min_max(complite))

# Решал преподаватель

# count = int(input('введите кол-во элементов: '))
# some_list = []

# for _ in range(count):
#     number = float(input())     # либо тут убрать float и тогда целые числа не бедет брать во внимание
#     some_list.append(number)
# maxx = 0
# minn = 1
# for el in some_list:
#     if '.' in str(el):
#         dr = str(el).split('.')[1]
#         if float('0.' + dr) > maxx:
#             maxx = float('0.' + dr)
#         elif float('0.' + dr) < minn:
#             minn = float('0.' + dr)
# print(maxx - minn)


# Задача 25 (ДЗ). Программа, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('введите число: '))
# b = ''
# while n > 0:
#     b += str(n % 2)
#     n //= 2
# print(b[::-1])

# Решал преподаватель
# # вариант 1:
# n = int(input('введите число: '))
# print(bin(n)[2:])                       # встроенна функция перевода
# [2:] это означает начать отображать со втрого символа(3ий) и до конца

# # вариант 2:
# n = int(input('введите число: '))
# b = ''
# while n != 0:
#     b += str(n % 2) + b                 # тут как-то прибавляя +b получился список развернутым, подумай
#     n //= 2                             # до этого все считал правильно, просто задом наперед, нужно было развернуть
# print(b)


# Задача 26 (ДЗ). Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def Fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# def NegaFibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = [0]
# userNumber = int(input('Enter any number: '))
# for e in range(1, userNumber + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)

# Решал преподаватель

# k = int(input())
# some_list = [0] * (k * 2 + 1)    # ЗАДАЕМ СПИСОК

# some_list[k + 1] = 1
# for idx in range(k + 2, k * 2 + 1):
#     some_list[idx] = some_list[idx - 1] + some_list[idx - 2]
# for idx in range(k, -1, -1):
#     some_list[idx] = some_list[idx + 2] - some_list[idx + 1]
# print(some_list)
