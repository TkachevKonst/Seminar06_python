# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# def geom_prog (a,b,c):
#     list_1 = []
#     for i in range(1, c+1):
#         list_1.append(a + (i - 1) * b)
#     return list_1
#
#
# a = int(input('Введите первый элемент: '))
# b = int(input('Введите шаг прогрессии: '))
# c = int(input('Введите количество элементов: '))
# print(*geom_prog(a,b,c))


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# from random import randint


# def section_list (list_1, minn, maxx):
#     index_1 = []
#     for i in range(len(list_1)):
#         if minn<list_1[i]<maxx:
#             index_1.append(i)
#     return index_1
#
#
# n = int(input('Введите количество элементов: '))
# minn = int(input('Введите начало диапозона: '))
# maxx = int(input('Введите конец диапозона: '))
# list_1 = [randint(0, 15) for i in range(n)]
# print(list_1)
# print(section_list(list_1,minn,maxx))