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

n = int(input('Введите число: '))
tot = 0
print(f'Для N = {n}:' '{')
for i in range (1, n + 1):
    tot += ((1 + 1 / i) ** i)
    print (*range(f'{i}:', tot), sep=', ')
    # print(tot)
print('}')
print(*range(-number, number + 1), sep=', ')

# Задача 17 (ДЗ).