# Задача 27. Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# a = some_list(map(int, input().split()))
# print(max(a), min(a))

# # второй вариант
# some_str = input()
# some_str = some_str.split()
# maxx = int(some_str[0])
# minn = int(some_str[0])
# for i in some_str:
#     if int(i) > maxx:
#         maxx = int(i)
#     elif int(i) < minn:
#         minn = int(i)
# print(minn, maxx)



# Задача 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

# # вариант 1:
# a, b, c = map(int, input().split())
# d = b**2 - 4 * a * c
# if d < 0:
#     print('решений нет')
# elif d == 0:
#     print(-b / (2 * a))
# else:
#     print((-b + d ** 0.5) / (2 * a))
#     print((-b - d ** 0.5) / (2 * a))

# # вариант 2:
# import sympy as sm

# a, b, c = map(int, input().split())
# x = sm.Symbol('x')                        # так нужно описывать например Х, если Y то писать 'Y', иначе не поймет
# print(sm.solveset(a * x ** 2 + b * x + c, x))

# Задача 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. 

# a, b = map(int, input().split())
# for i in range(min(a, b), a*b+1, min(a,b)):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break

# # второй вариант
# print(sm.lcm(int(input()), int(input())))


# ДОП Задача. Написать функцию thesaurus(), 
            # принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
            # в котором ключи — первые буквы имён, 
            # а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
            # >>> thesaurus("Иван", "Мария", "Петр", "Илья")
            # {
            # "И": ["Иван", "Илья"],
            # "М": ["Мария"], "П": ["Петр"]
            # }
            # Подумайте: полезен ли будет вам оператор распаковки? 
            # Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

# def num_translate(key, dictionary):
#     prime(dictionary[key])

# d = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь'}
# word = input('Write a word: ')
# num_translate(word, d)
# # вроде не доделали

# Задача 30 (ДЗ). Вычислить число c заданной точностью d

n = float(input('Введите число: '))
d = float(input('До скольки округлять: '))
if d == 1:
    print(int(n))
else:
    d = str(d)
    d = d.split('.')
    d = len(d[1])
    print(round(n, d))

# from decimal import Decimal

# def accuracy(num, acc):
#     number = Decimal(f'{num}')
#     return number.quantize(Decimal(f'acc'))

# print(accuracy(float(input('Введите real number: ')), float(input("enter 0.001: "))))

# Задача 31 (ДЗ). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input("Введите число: "))
# some_list = []
# i = 2 

# while number > 1:
#     if number % i == 0:
#         some_list.append(i)
#         number //= i
#     else:
#         i += 1

# print(f"Простые множители числа: {some_list}")

# Задача 32 (ДЗ). Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# a = [2, 5, 8, 8, 3, 0, 3, 2]
# b = []
# for i in a:
#     if a.count(i) == 1:    # ПОСМОТРЕТЬ ЧТО ТАКОЕ COUNT
#         b.append(i)

# print(b)

# Задача 33 (ДЗ). Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# from random import randint

# def RandomNaturalCoefficient():
#     numb = randint(0, 100)
#     return numb

# def FormingString(k):
#     res = f'{RandomNaturalCoefficient()}*x**{k} + {RandomNaturalCoefficient()}*x + 5 = 0'
#     return res

# userNumber = input('Set the natural power of the number: ')

# with open('Task 1\Data.txt', 'w') as data:
#     data.write(f'some_List of coefficients of a polynomial of degree {userNumber}:\n')
#     for i in range(10):
#         data.write(f'{FormingString(userNumber)}\n')

# import random

# k = int(imput())
# with open('res.txt', 'w') as a:
#     coef = []
#     for i in range(k + 1):
#         coef.append(random.randint(0, 100))
    


# Задача 34 (ДЗ). Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.