# Задача 1. На ввод два числа и проверка является ли одно число квадратом второго

# print('Является ли одно число квадратом второго?')
# a = input('Число 1 = ')
# b = input('Число 2 = ')
# if not a.isdigit() or not b.isdigit():   # Проверка что ввели цифру, а не букву
#     print('Ввели некорректное значение')
# else:
#     if int(a) ** 2 == int(b) or int(b) ** 2 == int(a):
#         print('является')
#     else:
#         print('не является')

# Задача 2. На ввод принимает 5 чисел и находит максимальное из них

# # первый способ
# some_list = max(map(int, input('Введите число через пробел: ').split()))
# # map - позволяет преобразовать строку(или то что вводится вторым после ,) в то что идет первым перед ,.
# # т.е. сейчас он преобразует введеные числа(а он думает что это строка) в INT.
# # split - разделяет строку на список строк, на основе разделителя (), в данном случае это пробел
# # max - встроенная функция, сразу ищет максимальное значение (сука сам ищет, пипец. В С# заибешся объяснять)
# print(some_list)

# # второй способ
# number = int(input())
# maxx = number
# for _ in range(4):     # здесь число 4 используется для прохода по циклу, т.е. 4 раза
#     number = int(input())
#     if number > maxx:
#         maxx = number
# print(f'максимальное число {maxx}')

# # третий способ
# some_list = []
# for _ in range(5):             # (5) это кол-во раз сколько повторятся этидействия в цикле
#     number = int(input())
#     some_list.append(number)   # метод append добавление числа (указывается в скобочках то число кот.хотим добавить) 
#                                # в список в данном случае some_list
# maxx = some_list[0]  # присваиваем макс значение
# for element in some_list:  # пройтичь по значениям в списке (в данном случае в сосзданом списке some_list)
#                            # т.е. занчение element будет принимать все сзанчения поочереди с 0, потом 1 и так до конца
#     if element > maxx:
#         maxx = element
# print(maxx)

# Задача 3. На ввод число N, и выводит числа от -N до N

# первый способ
# number = int(input('Введите число: '))
# for i in range(-number, number):  # тут убрали +1 в number, чтобы вывод был красивым, если оставить то след комент
#     print(i, end= ', ')  # end - делает символ после принта(в данном случае i), а какой указывается после ","
#                          # но так выводится и последняя ","  и будет всегда выводиться в отлии от "sep="
# print(number)            # в данном случае это строка используется как костыль

# втрой способ
# number = int(input('Введите число: '))
# print(*range(-number, number + 1), sep=', ') # распакавать range нужно поставить "*", т.е. без нее будет в выводе (-5, 5)
#                                              # грубо говоря * это range привести к списку (* равносильна list)
#                                              # sep= делает разделитель какой-то последовательности (range это и есть)

# Задача 4. На ввод дробное число, на выходе показывать первую цифру дробной части числа

# перый способ
# number = input('Введите число: ')
# if '.' not in number:
#     print('нет такой цифры')
# else:
#     num = (float(number) * 10) % 10
#     print(int(num))

# второй способ
# number = float(input('Введите число: '))
# if number % 1 == 0:
#     print('ввели не дробное число')
# else:
#     print(int(number * 10) % 10)

# третий способ
# number = input('Введите число: ')
# if '.' in number:
#     index_t = number.find('.') # index_t это переменная. number.find('.') это поиск интедекса какогото эл-та(строки)
#     print(number[index_t + 1])
# else:
#     print('ввели не дробное число')

# Задача 5. На ввод принимает число и проверяет его на кратность 5, 10, 15, но не 30.

# number = int(input('Введите число: '))
# if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
#     print('да') # если стоит много "and" и "or" то проверяются слачала and, а потом or. (как в математике + и *)
# else:
#     print('нет')

# Задача 6 (ДЗ). Программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# n = int(input('Введите цифирь: '))
# if n > 7 or n < 1:
#     print('Ввели неверное значение')
# elif n == 6 or n == 7:
#     print("Да, это выходной день")
# else:
#     print("Нет, работать!")

# Задача 7 (ДЗ). Программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Задача 8 (ДЗ). Программа, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = float(input('Введите координату X: '))
# y = float(input('Введите координату Y: '))

# if x == 0 and y == 0:
#     print('Нулевая точка координат')
# elif x > 0 and y > 0:
#     print('первая четверть')
# elif x < 0 and y > 0:
#     print('Точка во второй четверт')
# elif x < 0 and y < 0:
#     print('третья четверть')
# elif x > 0 and y < 0:
#     print('В четвертой четверти')

# Задача 9 (ДЗ). Программа, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('Введите номер четверти: '))
# if n < 1 or n > 4:
#     print('Ввели неверное значение')
# elif n == 1:
#     print('Диапазон координат от: x > 0 и y > 0')
# elif n == 2:
#     print('Диапазон координат от: x < 0 и y > 0')
# elif n == 3:
#     print('Диапазон координат от: x < 0 и y < 0')
# elif n == 4:
#     print('Диапазон координат от: x > 0 и y < 0')

# Задача 10 (ДЗ). Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1,y1=map(int,input('Введите координату первой точки через пробел: ').split())
x2,y2=map(int,input('Введите координату второй точки через пробел: ').split())
print(round(((x1-x2)**2+(y1-y2)**2)**0.5,2))