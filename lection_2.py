# первый способ записи файла
# colors = ['red', 'green', 'blue']   # [...] - некий набор данных (в данном случае список)
# data = open('file.txt', 'a')        # создаем текстовую переменную "data" и связываем ее с текстовым файлом
#                                     # 'file.txt' - тут указываем путь к файлу; "a" - мот с кот. будем работать
# # data.writelines(colors)             # разделителей не будет; 'writelines' - функционал позволяющий записать некоторый набор данных
# data.write ('LINE появится что-то с новой строки12\n')
# data.write ('LINE из-за того что поставили слэш21\n')
# data.close()                        # после того как поработали его нужно закрыть(разорвать связь)

# второй способ записи файла
# with open('file.txt', 'a') as data: # т.е "('file.txt', 'w')" вот эту конструкцию воспринимать как переменную "data"
#     data.write('line 12354511\n')
#     data.write('line8520\n')
# # тут если мы закрыли блок, close прописывать не нужно, он сам разорвет

# чтение файла
# path = 'file.txt'       # создадим путь к файлу
# data = open(path, 'r')  # открываем в режиме чтения "r"
# for line in data:       # при помощи цикла пробежимся по файлу и считаем все строки
#     print(line)
# data.close

# exit()                  # что бы код который ниже не выполнялся

# ФУНКЦИИ

# import lection_1 as h   # импортируем функцию из lection_1.py; 148 строка функция "f"
#                         # "as h" обзавем длинное название файла как "h"
# print(h.f(1))           # вместо "h" можно писать lection_1 если до этого не обозвали коротким именем

# РЕКУРСИЯ (там пипц)

# КОРТЕЖИ

a = (1, 2, 5, 85)
print(a)
print(a[-2])
# ОТЛИЧИЕ кортежа от списка тем что он не изменяем, т.е. если захотим присвоить a[0] = 12, он не даст это сделать

# СЛОВАРИ

# МНОЖЕСТВА

# colors = {'red', 'green', 'blue'}
# print(colors)                      # результат: {'red', 'green', 'blue'}
# colors.add('red')                  # .add - добавление         
# print(colors)                      # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)                      # {'red', 'green', 'blue','gray'}
# colors.remove('red')               # .remove - удаление
# print(colors)                      # {'green', 'blue','gray'}
#                                    # colors.remove('red') # KeyError: 'red'
# colors.discard('red')              # .discard - тоже удаление, но не выведет ошибку и прога пройдет дальше
# print(colors)                      # {'green', 'blue','gray'}
# colors.clear()                     # .clear - очищение множества {}
# print(colors)                      # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                         # .copy - копирование множества c = {1, 2, 3, 5, 8} 
u = a.union(b)                       # .union - объединение множества u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)                # дальше не объяснял i = {8, 2, 5}
dl = a.difference(b)                 # dl = {1, 3}
dr = b.difference(a)                 # dr = {13, 21}

q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}    "\" - обозначает переход кона на др строку

s = frozenset(a)                     # frozenset - замороженное множество
