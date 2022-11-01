# Задача 11. Программа, которая принимает на вход число N и выдаёт последовательность из N членов.

# n = int(input('Введите число: '))
# for i in range(n-1):
#     print((-3)**i, end=', ')
# else:
#     print((-3)**(n-1))

# # второй способ
# n = int(input('Введите число: '))
# a = []                             # создадим список "а"
# for i in range(n):
#     a.append((-3)**i)
# print(*a, sep=', ')                # выводим список и создаем сепаратор


# Задача 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# n = int(input('Введите число: '))
# array = []
# for i in range(1, n+1):
#     array.append(f'{i}: ' + str(3*i+1))
# print(array)

# # второй способ
# n = int(input())
# print('{', end='')
# for i in range(1, n):
#     print(f'{i}:{3 * i + 1}', end=', ')
# print(f'{n}:{3 * n + 1}', end='}')


# Задача 13. Программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# n1 = input('Введите строку: ')
# n2 = input('Введите строку: ')
# cnt = n1.count(n2)
# print(cnt)

# # втрой способ
# from itertools import count


# n1 = input('Введите строку: ')
# n2 = input('Введите строку: ')
# len_n2 = len(n2)
# i = 0
# count = 0
# while i < len(n1):
#     if n1[i:i+len_n2] == n2:
#         count += 1
#     i += 1
# print(count)

# Задача 14 (ДЗ). Программа, которая принимает на вход вещественное число и показывает сумму его цифр.

# хйяня какая то# n = input('Введите число: ')
# tot = 0
# for i in n:
#     if i != '.':
#         tot += int(i)
#     else:
#         n = float(n)
#         if n >= 1:
#             while n != 0:
#                 tot += int(n % 10)
#                 n //= 10
#         elif n < 0:
#             n = n * -1
#             while n != 0:
#                 tot += int(n % 10)
#                 n //= 10
#         else:
#             tot = 0 
# # 
# print(tot)
# ------------------------------------------------
# n = input('Введите число: ')
# tot = 0
# for symbol in n:
#     if symbol.isdigit():
#         tot += int(symbol)
# print(tot)
# ------------------------------------------------
# Задача 15 (ДЗ). Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число: '))
# pro = 1
# list1 = []
# for i in range(1, n + 1):
#     pro *= i
#     list1.append(int(pro))
# print(f'если N = {n}, тогда ', end=" ")
# print(list1)

# Задача 16 (ДЗ). Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите число: '))
# tot = 0
# print(f'Для N = {n}:' '{')
# for i in range (1, n + 1):
#     tot += ((1 + 1 / i) ** i)
#     print ((f'{i}:', tot), sep='')
#     # print(tot)
# print('}')
# # print(*range(-n, n + 1), sep=', ')
# # не получилось сделать вывод как в примере

# # второй способ
# n = int(input('Введите число: '))
# summ = 0
# for i in range(1, n + 1):
#     summ += (1 + 1 / i) ** i
# print(summ)

# Задача 17 (ДЗ). Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# хз
# import random

# n = int(input('Введите количество элементов: '))
# in_list = [i for i in range(n)]
# out_list = in_list[:]
# for i in range(n):
#     index_random = random.randint(0, n - 1)
#     temp = out_list[i]
#     out_list[i] = out_list[index_random]
#     out_list[index_random] = temp
# print('исходный список', in_list)
# print('перемешанный список', out_list)

# # второй способ
# from random import * # если я так пишу со звездочкой, то потом не нужно будет вызывать заново эту функцию,
#                      # она применится ко всему модулю (в данном случае seminar_2)
# n = int(input())
# some_list = []
# for _ in range(n):   # тут переменную использовать не будем, т.е. гонять по циклу не будем, 
#                      # а только используем цикл несколько раз, поэтому пишем _. Поидее она должна поменять n раз свои значения 
#     some_list.append(randint(-n, n))   # а вот тут сразу пишем рандит, т.к. выше использовали *
# print(some_list)
# with open('file.txt', 'w', encoding='utf-8') as f:   # encoding='utf-8 - кодировка для работы с латынью
#     for _ in range(n):
#         f.write(str(randint(0, n - 1)) + '\n')       # + '\n' сделать канкоканацию строк, т.е. сделать отступ на след строку
# fact = 1                                             # переменная для произведения
# with open('file.txt', 'r', encoding='utf-8') as f:
#     f = f.read().splitlines() # тут он переназначил f, и считал всю информацию которая записана и преобразовал к списку строк
#     for number in f:
#         fact *= some_list[int(number)]
# print(fact)

# Задача 18 (ДЗ). Реализуйте перемешиванием
import random   # вызовбиблиотеки

some_list = [1, 7, 8, 4, 9, 10]
random.shuffle(some_list)   # Команда из библиотеки перемешивания
print(some_list)
