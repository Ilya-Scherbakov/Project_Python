print("Hello world")
# print('введите a')
# a = float(input())
# print('введите b')
# b = float(input())
# print(a, '+', b, '=', a+b)

# print('{} {}'. format(a, b)) примеры возможного вывода данных
# print(f'{b} {a}')            примеры возможного вывода данных

# Арифмитические операции
# +, -, *, /, %, //, **
#
a = 12
b = 7
# деление вещественного числа
# c = a/b
# деление целого числа
# c = a//b
# получение остатка от деления
# c = a % b
# возведение в степень первого числа
# c = a**b
# окрегление по мат. законам. указывается кол-во цифр после запятой
c = round(a/b, 7)
print(c)

a = 5
a += 7
# оператор присваивания, получим 12.
print(a)
#  Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, ^, |
#
# a = 1 > 3
# в выводе получим false или true
a = 1 < 4 and 5 > 2
# a = 1 > 4 or 5 > 2 тут тоже будет true, потому что выбор чегото одного
# a = 1 == 2
# a = 1 != 2
# a = 1 < 3 < 5
print(a)
# a = `qwe` b = `qwe`
a = [1, 2]
b = [1, 2]
# можем сравнивать строки и списки
print(a == b)

f = [1, 2, 3, 4]
print(f)
print(not 2 in f)
# поиск указанного числа в списках
is_odd = f[0] % 2 == 0
# проверка на четность первого (нулевого) числа в списке
print(is_odd)

# Управляющие конструкции: if, if-else (ЦИКЛЫ)
print('Нахождение максимального числа')
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

print('оператор ветвления')
username = input('введите имя: ')
if username == 'Маша':
    print('Ура, это Маша!!')
elif username == 'Марина':
    print('Я так ждал Вас, Марина')
elif username == 'Илья':
    print('Илья - ТОП')
else:
    print('Привет, ', username)

# Управляющие конструкции: while, for (ЦИКЛЫ)

# разворачиваем число
original = 203
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# переменная i сносим занчения(список), а потом выводим квадрат каждого числа
# for i in 1,2,3,3,5:
#     print(i**2)
# или
for i in range(1, 12, 2):
    print(i)
# так же со строками
# for i in 'qwerty':
#     print(i)

# Немного о строках

text = 'съешь еще этих мягких французских булок'
print(len(text))                        # 39, len - длина строки, или кол-во символов
print('еще' in text)                    # True, поиск определенных символов
print(text.isdigit())                   # False, все символы строки числа?
print(text.islower())                   # True, все символы строки нижнего регистра?
print(text.replace('еще','ЕЩЕ'))        # Заменить одно на другое
help(text.istitle)                      # Справка функции которую мы не знаем, вообще для всего
print(text[0])                          # c, покажет 0 заначение массива
print(text[1])                          # ъ, покажет 1 занчение массива
print(text[len(text)])                  # IndexError, ошибку, потому идексация с нуля, х/з что это
print(text[len(text)-1])                # к, покажет последенее занчение массива
print(text[-5])                         # б, покажет 5 с конца занчение
print(text[:])                          # print(text), это сокращение, по факту типо стоят аргументы text[0:len(text)-1], т.е. от 1 до последнего
print(text[:2])                         # съ, т.е. от 0 до 2 го символа
print(text[len(text)-2:])               # ок
print(text[2:9])                        # ешь ещё
print(text[6:-18])                      # ещё этих мягких
print(text[0:len(text):6])              # сеикакл
print(text[::6])                        # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...

# Списки

numbers = [1, 2, 3, 4, 5]
print(numbers)                      # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)                      # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)                      # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i)                           # [20, 4, 6, 8, 10]
print(numbers)                      # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e)                                           # red green blue
for e in colors:
 print(e*2)                                         # redred greengreen blueblue
colors.append('gray')                               # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])   # True
colors.remove('red')                                #del colors[0] # удалить элемент

# ФУНКЦИИ

def f(x):
 return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28)))