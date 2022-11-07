import numbers
from re import T
from unittest.mock import patch


def f(x):
    return x**2

g = f
print(f(2))
print(g(2))

print(type(f))
print(type(g))

# ------------------

# Какие-то КОМПРЕХЕНЦИИ

list = []                                                 # Классическое создание списка напр. четных чисел

for i in range(1, 101):
    if (i % 2 == 0):
        list.append(i)

print(list)

list = [i for i in range(1, 101) if i % 2 == 0]           # Так можно это коротко описать
print(list)

def f(x):
    return x**3

list = [f(i) for i in range(1, 101) if i % 2 == 0]        # А тут будет уже подставлять кубы из пред. функции и писать только %2
print(list)

list = [(i, f(i)) for i in range(1, 101) if i % 2 == 0]   # А тут будет уже КОРТЕЖ. число и его куб
print(list)

# -------------------------

# Задача: В файле хранятся числа, нужно выбрать четные и составить список пар (число, квадрат числа)

path = "тут указать путь к файлу"
f = open(path, 'r')    # тут типо присваеваем и назанчаем читать
data = f.read() + ' '  # тут он считывает все что есть в строчке и добвляет пробел 
f.close()

numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
    
out = []
for e in numbers:
    if not e % 2:
        out.append((e,e **2))
print(out)

# ТЕПЕРЬ РЕШИТЬ ПОДРУГОМУ ЛЯМБДАМИ 

def select(f, col):   # принимает функцию f, и какойто набор данных
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2 , res)
res = select(lambda x: (x, x**2), res)
print(res)

# ДАЛЬШЕ ОН ЕЕ РЕШАЛ ЧЕРЕЗ MAP, Я НЕ ЗАПИСЫВАЛ

