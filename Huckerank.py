# Задача 1
# n = int(input().strip())
# if n % 2 == 0:
#     print("Not Weird")
# else:
#     print("Weird")
#

# Задача 2
# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)


# Задача 3
# a = int(input())
# b = int(input())
# print(a // b)
# print(a / b)


# Задача 4
# def is_leap(year):
#     if year % 4 > 0:
#         if year % 400 > 0:  # Write your logic here
#             return False
#
#
# year = int(input())
# print(is_leap(year))


# Задача 5
# n = int(input())
# for n in range(1, n + 1):
#     print(n, end="")


# Задача 6
# кубоид
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# ar = []
# p = 0
# for i in range(x + 1):
#     for j in range(y + 1):
#         for z in range(z + 1):
#             if i + j + z != n:
#                 ar.append([])
#                 ar[p] = [i, j, z]
#                 p += 1
# print(ar)


# Задача 7
# numbers = [2, 3, 6, 6, 5]
# number = int(input())
# print(numbers[number - 1])


# Задача 8
# numbers = [['Krishna', 67, 68, 69], ['Arjun', 70, 98, 63], ['Malika', 52, 56, 60]]
# p = (input())
# n = 3
# numbers_n = numbers[n - 1]
# num = 0
# for i in range(1, len(numbers_n)):
#     num += numbers_n[i]
# result = num / 3
# p = result
# print(format(p, '.2f'))
#
# numbers_two = [['Harsh', 25, 26.5, 28], ['Anurag', 26, 28, 30]]
# n2 = 2
# p2 = (input())
# numbers_n2 = numbers_two[n2 - 2]
# num2 = 0
# for i2 in range(1, len(numbers_n2)):
#     num2 += numbers_n2[i2]
# result2 = num2 / 3
# p2 = result2
# print(format(p2, '.2f'))

# Задача 9
# numbers = []
# numbers.insert(0, 5)
# numbers.insert(0, 6)
# numbers.insert(1, 10)
# box = []
# for i in range(len(numbers)):
#     box.append(numbers[i])
# box[1], box[2] = box[2], box[1]
# print(box)
# box.remove(6)
# box.append(9)
# box.append(1)
# box.sort()
# print(box)
# box.pop(3)
# box.reverse()
# print(box)

# Задача 10
# integer = int(input())
# num = []
# for integer in range(1, integer + 1):
#     num.append(integer)
# print(hash(tuple(num)))
# number = tuple(range(1, int(input()) + 1))
# print(hash(number))

# Заглавные быквы задача 11
# number = (input())
# box = []
# for word in number:
#     if word.isupper():
#         box.append(word.lower())
#     else:
#         box.append(word.upper())
# for words in box:
#     print(words, end="")

# Задача 12 склеивание
# def word():
#     a = "this is a string"
#     a = a.split()
#     p = "-"
#     return p.join(a)
#
#
# print(word())

# Задача 13 ввод имени поль
# name = input()
# lastName = input()
# print("Hello", name, lastName + "!", "You just delved into python.")

# Задача 13(2 способ)
# def print_full_name(a, b):
#     print("Hello", first_name, last_name + "!", "You just delved into python.")
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


# Задача 14 где 5 индекс склеивать другую букву
# 1
# s = input()
# i, c = input().split()
# i = int(i)
# s = list(s)
# s[i] = c
# s = "".join(s)
# print(s)
# 2
# string = "abracadabra"
# l = list(string)
# l[5] = 'k'
# str1 = ''.join(l)
# print(str1)
# abrackdabra
#
# 3
# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra
# 4
# def mutate_string(string, position, character):
#     sr = list(s)
#     b = s[i]
#     b = c
#     return sr
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# Задача 15 считать количество букв в строке
# def count_substring(a, b):
#     box = 0
#     for ln in range(1, len(sub_string) + 1):
#         box = ln
#     return box
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)


# Задача 16 если хотя бы одна буква входит в условия
# st = input()
# print(st.isalnum())
# bol = []
# for i in st:
#     if i.isalpha():
#         print(True)
#         break
# for i in st:
#     if i.isdigit():
#         print(True)
#         break
# for i in st:
#     if i.isupper():
#         print(True)
#         break
# for i in st:
#     if i.islower():
#         print(True)
#         break

# метод сдвид на право, лево, центр
# n = int(input())
# print("Hello".rjust(n, "-"))
# print("Hello".center(n, '-'))
# print("Hello".ljust(n, '-'))


# Задача 17
# words = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# n = 4
# box_word = []
# for words in words:
#     box_word.append(words)
# box_11 = [[], [], [], [], [], []]
# for t in range(len(box_word)):
#     if t <= n - 1:
#         box_11[0].append(box_word[t])
#     if 3 < t < 8:
#         box_11[1].append(box_word[t])
#     if 8 < t < 13:
#         box_11[2].append(box_word[t])
#     if 13 < t < 18:
#         box_11[3].append(box_word[t])
#     if 18 < t < 23:
#         box_11[4].append(box_word[t])
#     if 23 < t < 26:
#         box_11[5].append(box_word[t])
# for words in box_11:
#     print("".join(words))

# задача 18
# name = input()
# last_name = input()
# last_name = list(last_name)
# name = list(name)
# for i_name in name[0]:
#     if i_name.islower():
#         b = i_name.upper()
#         name[0] = b
# for nam in last_name[0]:
#     if nam.islower():
#         c = nam.upper()
#         last_name[0] = c
# print("".join(name), "".join(last_name))


# Задача 19
# words1 = [['B'], ['N'], ['BA'], ['NA'], ['BAN'], ['NAN'], ['BANA'], ['NANA'], ['BANAN'], ['BANANA']]
# sp_w1 = [1, 2, 1, 2, 1, 1, 1, 1, 1, 1]
# words2 = [['A'], ['AN'], ['ANA'], ['ANAN'], ['ANANA']]
# sp_w2 = [3, 2, 2, 1, 1]
# box1 = 0
# box2 = 0
# for i1 in sp_w1:
#     box1 += i1
#     for i2 in sp_w2:
#         box2 += i2
# if box1 > box2:
#     print(box1)
# else:
#     print(box2)


# Алгоритм свига на право
# s = [1, 2, 3, 4, 5]
# n = 5
# tmp = s[0]
# for k in range(n - 1):
#     s[k] = s[k + 1]
# s[n - 1] = tmp
# print(s)

# сдвиг направо
# s = [1, 2, 3, 4, 5]
# n = 5
# tmp = s[n - 1]
# for k in range(n-2, -1, -1):
#     s[k + 1] = s[k]
# s[0] = tmp
# print(s)


# Задача 20
# st = input()
# num = int(input())
# ls = list(st)
# stp = []
# for words in range(0, len(ls), 1):
#     stp.append(words)
# stp = []
# for i in range(num):
#     stp.append([])
# for i2 in range(len(ls)):
#     if i2 < 3:
#         stp[0].append(ls[i2])
#     elif 2 < i2 < 6:
#         stp[1].append(ls[i2])
#     elif 5 < i2 <= 8:
#         stp[2].append(ls[i2])
# box = []
# for i in range(len(stp)):
#     if stp[i][0] != stp[i][2]:
#         box.append([stp[i][0], stp[i][2]])
#     if stp[i][0] == stp[i][2]:
#         box.append([stp[i][0], stp[i][1]])
# for st in box:
#     print("".join(st))

# Задача 21
# number = int(input())
# numbers = list(map(int, input().split()))
# number_pol = int(input())
# num1 = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
# num2 = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
# num1.sort()
# p = 0
# box = []
# for i1 in range(len(num1) - 1):
#     for i3 in numbers:
#         if num1[i1][0] == i3:
#             if p < 3:
#                 box.append(num1[i1][1])
#                 p += 1
# result = 0
# for box in box[0], box[2]:
#     result += box
# for i2 in range(len(num2)):
#     for i4 in numbers:
#         if num2[i2][0] == i4:
#             result += num2[i2][1]
# print(result)

# Задача 22
# box = []
# for num1 in range(2, 101):
#     for num2 in range(2, 101):
#         result = num1 ** num2
#         box.append(result)
# print(len(set(box)))

# Задача 23
# from itertools import permutations
#
# words = input()
# W = int(input())
# words = list(words)
# b = list(permutations(words))
# c = set(b)
# box = [x for x in c]
# box_two = []
# box_three = []
# for i in range(len(box)):
#     box_two.append([box[i][0], box[i][1]])
# for i1 in range(len(box)):
#     box_three.append([box[i1][2], box[i1][3]])
# result2 = box_two + box_three
# result1 = []
# for j in range(len(result2)):
#     result1.append(''.join(result2[j]))
# result_two = set(result1)
# for result_two in result_two:
#     print(result_two)


# Задача 24
# from cmath import phase
# from abc import ABC
# print(phase(complex(1.0, 2.0)))

# Лабороторная 1(2)
# number = ['mix', 'xyz', 'apple', 'xanadu', 'aardvard']
# number.sort()
# box = []
# for i in range(len(number)):
#     box.append([])
#     for b in number[i]:
#         box[i].append(b)
# box_two = [box[i2] for i2 in reversed(range(len(box)))]
# for it in range(len(box_two) - 1):
#     if box_two[it][0] == 'm':
#         box_two[it], box_two[it + 1] = box_two[it + 1], box_two[it]
# box_three = []
# for w in range(len(box_two)):
#     box_three.append(''.join(box_two[w]))
# print(box_three)

# number = [1, 2, 2, 3, 3]
# box = []
# for ind in range(len(number) - 2):
#     if number[ind] == number[ind + 1]:
#         del number[ind]
#         print(number)

# Лабороторная 1(3)
# number = [1, 2, 2, 3, 4]
# n = len(number) - 1
# box = []
# for ind in range(len(number) - 1):
#     if number[ind] != number[ind + 1]:
#         box.append(number[ind])
# box.append(n)
# print(box)

# Лабороторная 1(4)
# number = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# number[len(number) - 1], number[len(number) - len(number)] = number[len(number) - len(number)], number[len(number) - 1]
# print(number)

# Лабороторная 1(5)
# n1 = [10, 1, 6, 7, 15]
# n2 = [5, 4, 9, 8, 2, 3]
# print(sorted(n1 + n2))

# Лабороторная 2(1)
# word = input()
# box = [x for x in word]
# r = len(box) - 2
# s = len(box) - r
# result = []
# for i in range(s):
#     result.append(box[i])
# a = len(box) - 2
# b = 2 + a
# for i2 in range(a, b):
#     result.append(box[i2])
# print(''.join(result))


# Лабороторная 2(2)
# words = 'babble'
# word = [w for w in words]
# s = '*'
# result = []
# for word2 in range(0, 2):
#     result.append(word[word2])
# result2 = []
# for word3 in range(2, len(word)):
#     result2.append(word[word3])
# b = ''.join(result2)
# c = b.replace('b', '*')
# for a in c:
#     result.append(a)
# print(''.join(result))

# Лабороторная 2(3)
# word_one1 = input()
# word_two2 = input()
# word_one = [w1 for w1 in word_one1]
# word_two = [w2 for w2 in word_two2]
# yes = 0
# no = 0
# for i1 in range(len(word_one)):
#     for i2 in range(len(word_two)):
#         if word_one[i1] == word_two[i2]:
#             yes += 1
#         elif word_one[i1] != word_two[i2]:
#             no += 1
# if yes > 0:
#     print(word_one1.replace(word_one[1], word_two[1]), word_two2.replace(word_two[1], word_one[1]))
# if yes == 0:
#     print(word_two2.replace(word_two[len(word_two) - 1], word_one[len(word_one) - 1]),
#           word_one1.replace(word_one[len(word_one) - 1], word_two[len(word_two) - 1]))

# Лабороторная 2(3)
# word = input()
# n = 2
# w1 = 'ing'
# w2 = 'ly'
# word_copy = [w for w in word]
# if len(word_copy) - 1 >= 2:
#     a = len(word_copy) - 3
#     box = []
#     for i in range(a, len(word_copy)):
#         box.append(word_copy[i])
#     box = ''.join(box)
#     if box == w1:
#         print(word.replace(w1, w2))
#     else:
#         print(word + w1)
# elif len(word_copy) - 1 < 3:
#     print(word)


# Лабороторная 2(4)
# word = 'This dinner is not that bad!'
# box = []
# bad = 'bad'
# now = 'not'
# good = ['good!']
# p = 6
# for i in range(7):
#     box.append([])
# for i1 in range(len(word)):
#     if i1 < 4:
#         box[p - p].append(word[i1])
#     if 4 < i1 < 11:
#         box[p - 5].append(word[i1])
#     if 11 < i1 < 14:
#         box[p - 4].append(word[i1])
#     if 14 < i1 < 18:
#         box[p - 3].append(word[i1])
#     if 18 < i1 < 23:
#         box[p - 2].append(word[i1])
#     if 23 < i1 < 27:
#         box[p - 1].append(word[i1])
#     if 26 < i1 < 28:
#         box[p - 0].append(word[i1])
# result = []
# r1_b = 0
# r2_n = 0
# for w in box:
#     result.append(''.join(w))
# for res in range(len(result)):
#     if result[res] == bad:
#         r1_b += res
#     if result[res] == now:
#         r2_n += res
# bob_box = []
# if r2_n < r1_b:
#     for t in range(len(result) - 4):
#         bob_box.append(result[t])
# bob_box = bob_box + good
# for b in bob_box:
#     print(b, end=' ')


# Лабороторная 2(4)
# word1 = input()
# word2 = input()
# word_1 = [w1 for w1 in word1]
# word_2 = [w2 for w2 in word2]
# result = len(word_1) + len(word_2)
# rs = len(word_1) // 2
# rs1 = len(word_2) // 2
# res = []
# n = 0
# p = 0
# for i1 in range(rs):
#     res.append([])
# if result % 2 == 0:
#     for i in word_2:
#         res[p].append(i)
#         n += 1
#         if n == 2:  # алгоритм разбиения строки по константному символу разбиение
#             n -= 2
#             p += 1
#             r1 = res[0][0]
#             r2 = word1[2]
#             r3 = word1[3]
#             m = word1.replace('c', r1)
#             m1 = m.replace('d', r2)
#             m3 = word2.replace('x', r3)
#             print(m1 + m3)
# else:
#     for i1 in range(rs1):
#         res.append([])
#     if result % 2 != 0:
#         for i in word_1:
#             res[p].append(i)
#             n += 1
#             if n == 3:  # алгоритм разбиения строки по константному символу разбиение
#                 n -= 3
#                 p += 1
#                 r1 = res[1]
#                 kit = res[0]
#                 kit = ''.join(kit)
#                 r2 = ''.join(r1)
#                 m1 = word2.replace('ut', r2)
#                 ut = word2[3], word2[4]
#                 ut = ''.join(ut)
#                 print(kit + m1 + ut)
# import re
# a = ['43644213']
# b = re.findall(r'\d\d\d', a)
# print(b)


# Лабороторная 3
# from collections import Counter
#
#
# def func(print_words, word):
#     if print_words == 'count':
#         return Counter(word)
#     if print_words == 'topcount':
#         return Counter(word)
#
#
# print(func(input(), input().split()))

# number = [1, 2, 2, 3, 4]
# print(*Counter(number))


# Работа с календарем
# from collections import defaultdict

# words = "apple banana apple strawberry banana lemon"
# d = defaultdict(int)
# for word in words.split():
#     d[word] += 1
# print(d)


# import calendar
#
# # # Создаем обычный текстовый календарь
# c = calendar.TextCalendar(calendar)
# str = c.formatmonth(2025, 1, 0, 0)
# for i in str.
# print(str)
# #
# Создаем календарь в формате HTML
# hc = calendar.HTMLCalendar(calendar.THURSDAY)
# str = hc.formatmonth(2025, 1)
# print(str)
# перебираем через цикл дни месяца
# нули указывают, что дни принадлежат смежному месяцу
# for i in c.itermonthdays(2025, 4):
#     print(i)
#
#     # Календарь может выдавать информацию на основе локальных настроек, таких как название дней и месяцев (полных или сокращенных)
#     for name in calendar.month_name:
#         print(name)
#     for day in calendar.day_name:
#         print(day)
#     # вычисляем день на основе правил: Например для каждого второго понедельника каждого месяца
#     # Устанавливаем это для каждого месяца, мы можем использовать следующий скрипт
#     for month in range(1, 13):
#         # Он извлекает список недель, который представляет месяц
#         mycal = calendar.monthcalendar(2025, month)
#         # Первый MONDAY должен принадлежать первой или второй неделе
#         week1 = mycal[1]
#         week2 = mycal[2]
#         if week1[calendar.MONDAY] != 0:
#             auditday = week1[calendar.MONDAY]
#         else:
#         # если первый MONDAY не принадлежит первой неделе, он должен быть на второй неделе
#         auditday = week2[calendar.MONDAY]
# print("%10s %2d" % (calendar.month_name[month], auditday))


# Каленьдарь
# import calendar
#
# a = calendar.weekday(2020, 5, 5)
# print(a)

# import datetime
# import calendar
#

# Задача 25
# mydate = "05.05.2020"
#
# workdate = datetime.datetime.strptime(mydate, "%d.%m.%Y")
# print(calendar.day_abbr[workdate.date().weekday()])

# Выводим поностью календарь
# import calendar
# print(calendar.TextCalendar(firstweekday= 6 ) .formatyear(2015))


# Задача 26
# c = int(input())
# d = '$'
# try:
#     print(c // d)
# except TypeError as e:
#     print("Ошибка:", e)
# c = int(input())
# d = int(input())
# try:
#     print(c // d)
# except ZeroDivisionError as e:
#     print("Ошибка:", e)
#
# c = int(input())
# d = int(input())
# try:
#     print(c // d)
# except ZeroDivisionError as e:
#     print("Ошибка:", e)


# Задача 27 namedtuple
# from collections import namedtuple
#
# Car = namedtuple('Car', 'Price Mileage Colour Class')
# xyz = Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# print(xyz)
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# print(xyz.Class)


# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# print(dot_product)


# Задача 27
# from collections import namedtuple
#
# Car = namedtuple('Person', 'ID MARKS NAME CLASS')
# person1 = Car(ID=1, MARKS=97, NAME='Raymond', CLASS=7)
# person2 = Car(ID=2, MARKS=50, NAME='Steven', CLASS=4)
# person3 = Car(ID=3, MARKS=91, NAME='Adrian', CLASS=9)
# person4 = Car(ID=4, MARKS=72, NAME='Stewart', CLASS=5)
# person5 = Car(ID=5, MARKS=80, NAME='Peter', CLASS=6)
# result = (person1.MARKS + person2.MARKS + person3.MARKS + person4.MARKS + person5.MARKS) / 5
# print(result)

# Задача 28 прямоугольный треугольник
# ABC = 90
# AB = BC = int(input())
# MBC = ABC // 2
# print(MBC)


# Задача 29
# m = input().split()
# numbers_rand = input().split()
# numbers_A, numbers_B = input().split(), input().split()
# i = 0
# for n in numbers_rand:
#     if n in numbers_A:
#         i += 1
#     if n in numbers_B:
#         i -= 1
# print(i)

# Задача 30 менеджер в магазине
# from collections import OrderedDict
#
# size = int(input())
# ordered_dictionary = OrderedDict()
# i = 0
# while i < size:
#     ordered_dictionary[input()] = int(input())
#     i += 1
# val = set(v for v in ordered_dictionary)
# sl = OrderedDict()
# for v in val:
#     sl[v] = 0
# box1 = [zsl for zsl in val]
# box2 = [zr for zr in ordered_dictionary.keys()]
# r = 0
# n = 0
# p = 0
# u = 0
# ab = sl
# result =[]
# while r < len(box1) - 1:
#     for h in range(len(box2)):
#         if p < len(box2):
#             p += 1
#             u += 1
#             if box1[n] == box2[h]:
#                 ab[box1[n]] += ordered_dictionary[box2[h]]
#         else:
#             ab[box1[n]] += ordered_dictionary[box2[h]]
#             p -= len(box2)
#             n += 1
#             r += 1
# print(u)

# Функция объеденения и пересечения
# >> a = {2, 4, 5, 9}
# >> b = {2, 4, 11, 12}
# >> a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}
# >> a.intersection(b) # Values which exist in a and b
# {2, 4}
# >> a.difference(b) # Values which exist in a but not in b
# {9, 5}

# Задача 31 симметричная разност
# number1, numbers1 = int(input()), set(map(int, input().split()))
# number2, numbers2 = int(input()), set(map(int, input().split()))
# rev = numbers1.difference(numbers2), numbers2.difference(numbers1)
# result = []
# for i in rev:
#     result.append(*i)
# print(result)


# >>> from itertools import combinations
# # >>>
# # >>> print list(combinations('12345',2))
# # [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
# # >>>
# # >>> A = [1,1,3,3,3]
# # >>> print list(combinations(A,4))
# # [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

# Задача 32 Сочетание
# from itertools import combinations
# wr = input().split()
# wrd = []
# for w in wr:
#     if w.isalpha():
#         wrd.append(w)
# result_one = list(combinations(*wrd, 1))
# result_two = list(combinations(*wrd, 2))
# box = []
# for i in range(len(result_two)):
#     box.append(''.join(result_two[i]))
# box_two = []
# for word in result_one:
#     box_two.append(*word)
# result = box_two + box
# for word in result:
#     print(word)


# Регулярные выражения!
# . - любой одиночный символ
# [ ] - любой из них, диапазоны
# $ - конец строки
# ^ - начало строки
# \ - экранирование
# \d - любую цифру
# \D - все что угодно, кроме цифр
# \s - пробелы
# \S - все кроме пробелов
# \w - буква
# \W - все кроме букв
# \b - граница слова
# \B - не границ
#
# Квантификация
# n{4} - искать n подряд 4 раза
# n{4,6} - искать n от 4 до 6
# * от нуля и выше
# + от 1 и выше
# ? - нуль или 1 раз

# Задача 33
# number = int(input())
# i = 0
# box = []
# while i < number:
#     numbers = input()
#     box.append(numbers)
#     i += 1
# print(len(set(box)))

# Задача 34
# from collections import Counter
#
# number = int(input())
# i = 0
# box = []
# while i < number:
#     numbers = input()
#     box.append(numbers)
#     i += 1
# res = Counter(box).values()
# numbers = [x for x in res]
# print(len(numbers))
# print(*numbers)
# from collections import deque
#
# number = int(input())
# numbers = deque()
# i = 0
# while i < number:
#     numbers.append(1)
#     numbers.append(2)
#     numbers.append(3)
#     numbers.appendleft(4)
#     i += number
# numbers.pop()
# numbers.popleft()
# print(*numbers)


# Задача 35
# from collections import Counter
# words = input()
# words = list(words)
# word = Counter(words).most_common(3)
# for w in word:
#     print(*w)

# Задача 36
# fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# print(fib(31))

# Задача 37
# students1, eng = int(input()), set(input().split())
# students2, fr = int(input()), set(input().split())
# print(len(set(eng | fr)))

# Задача 38
# students1, eng = int(input()), set(input().split())
# students2, fr = int(input()), set(input().split())
# print(len(eng & fr))

# Задача 39 расстановка кубиков
# number_op = int(input())
# w = 0
# while w < number_op:
#     kol_box, len_box = int(input()), list(map(int, input().split()))
#     l_box = kol_box // 2
#     r_box = kol_box - l_box
#     u = 0
#     if l_box < r_box:
#         sm = r_box - l_box
#         r_box -= sm
#         u = 1
#
#     cr = []
#     c = reversed(len_box)
#     for r in c:
#         cr.append(r)
#
#     st = []
#     for i in range(l_box):
#         t1 = len_box[i]
#         t2 = cr[i]
#         if t1 >= t2:
#             st.append(t1)
#             st.append(t2)
#             continue
#         elif t1 <= t2:
#             st.append(t1)
#             st.append(t2)
#             continue
#     if u == 1:
#         st.append(cr[r_box - 1])
#     yes = 1
#     for p in range(len(st) - 1):
#         if st[p] >= st[p + 1]:
#             st[p] += 1
#             yes += 1
#         else:
#             print('No')
#             w += 1
#             break
#     if yes == len(st):
#         print('Yes')
#         w += 1

# Задача 40 расстановка кубиков
# number = int(input())
# con = []
# for i in range(1, number + 1):
#     con.append([])
#     for j in range(1, i + 1):
#         con[i - 1].append(j)
# for i1 in range(1, len(con)):
#     pr = con[i1]
#     for j1 in range((len(pr) - 2), -1, -1):
#         pr.append(pr[j1])
# for i in con:
#     print(*i, sep='')


# Задача 40
# a, b = int(input()), int(input())
# rd, ro = a // b, a % b
# print(rd, ro, divmod(a, b), sep='\n')

# 41
# K, M = map(int, input().split())
# st1, st2, st3 = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
# print(((max(st1) ** 2) + (max(st2) ** 2) + (max(st3) ** 2) % M))
#
# >>> s = set("Hacker")
# >>> print s.difference("Rank")
# set(['c', 'r', 'e', 'H'])


# 42
# n, numbers = int(input()), set(map(int, input().split()))
# n2, numbers2 = int(input()), set(map(int, input().split()))
# print(len(numbers ^ numbers2))


# .intersection_update() или &= Обновите набор, сохранив только элементы, найденные в нем, и повторяемый/другой набор.
# > > > > > > > >  H =  set("Hacker")
# >>>>>>>>>  R =  set("Rank")
# >>>>>>>>>  H.intersection_update( R)
# >>>>>>>>>  print
# Hset(['a',  'k'])

# .update() or |= Обновите
# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.update(R)
# >>> print H
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])


# .difference_update() or -= Обновите набор, удалив элементы, найденные в повторяющемся / другом наборе.
# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.difference_update(R)
# >>>
# set(['c', 'e', 'H', 'r'])


# .symmetric_difference_update() or ^=  Обновите набор, сохраняя только элементы, найденные в любом наборе, но не в обоих.

# n = set(input().split()) котор содерж в одном
# n2 = set(input().split())
# print(n.difference(n2))

# n = set(input().split())  котор содерж в одном
# n2 = set(input().split())
# print(n.intersection(n2))

# 43
# n1, numbers1 = int(input()), set(input().split())
# num = int(input())
# s1 = input()
# numbers2, s2 = set(input().split()), input()
# numbers3, s3 = set(input().split()), input()
# numbers4, s4, numbers5 = set(input().split()), input(), set(input().split())
# numbers1.intersection_update(numbers2)
# numbers1.update(numbers3)
# numbers1.symmetric_difference_update(numbers4)
# numbers1.difference_update(numbers5)
# n = 0
# for i in numbers1:
#     n += int(i)
# print(n)

# 44
# number = int(input())
# n = 1
# for i in range(1, number + 1):
#     print(*[i] * n, sep='')
#     n += 1

# 45
# from collections import Counter
#
# n, numbers = int(input()), Counter(input().split())
# for i in numbers:
#     if numbers[i] == 1 or numbers[i] == 0:
#         print(i)

# 46
# n1 = int(input())
# num1, numbers1 = int(input()), set(input().split())
# num2, numbers2 = int(input()), set(input().split())
# num3, numbers3 = int(input()), set(input().split())
# num4, numbers4 = int(input()), set(input().split())
# num5, numbers5 = int(input()), set(input().split())
# num6, numbers6 = int(input()), set(input().split())
# for i1 in numbers1:
#     if i1 in numbers2:
#         print('True')
#         break
#     else:
#         print('False')
#         break
# for i2 in numbers3:
#     if i2 in numbers4:
#         print('True')
#         break
#     else:
#         print('False')
#         break
# for i3 in numbers5:
#     if i3 in numbers6:
#         print('True')
#         break
#     else:
#         print('False')
#         break


# 47
# numbers = input().split()
# num, numbers1, numbers2 = int(input()), input().split(), input().split()
# for i in numbers1:
#     if i in numbers2:
#         print('True')
#         break
#     else:
#         print('False')
#         break

# 48
# n1, n2 = input().split()
# numbers1, numbers2 = map(float, input().split()), map(float, input().split())
# numbers3 = map(float, input().split())
# box = []
# n = 0
# i = 0
# for i1 in numbers1:
#     for i2 in numbers2:
#         for i3 in numbers3:
#             n += i1 + i2 + i3
#             n //= 3
#             box.append(n)
#             n = 0
# for i in box:
#     i = int(i)
#     print(i)


# for t in range(len(st) - 1):
#     if st[t] == st[t + 1]:
#         s2[n] += 1
#     elif st[t] != st[t + 1]:
#         s2[n + 1] += 1
#         n += 1

# 49 zip()
# >>> print zip([1,2,3,4,5,6],'Hacker')
# [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
# >>>
# >>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
# [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
# >>>
# >>> A = [1,2,3]
# >>> B = [6,5,4]
# >>> C = [7,8,9]
# >>> X = [A] + [B] + [C]
# >>>
# >>> print zip(*X)
# [(1, 6, 7), (2, 5, 8), (3, 4, 9)]

# 50
# sub, person = int(input()), int(input())
# box = []
# for b in range(person):
#     box.append([])
# t = 0
# for p in range(person):
#     for i in range(sub):
#         n = float(input())
#         box[t].append(n)
#         if i == sub - 1:
#             t += 1
#     continue
# nums = [0.0] * person
# z = 0
# d = 0
# for i in range(len(box)):
#     n = box[i]
#     for i1 in n:
#         nums[z] += i1
#         z += 1
# print(nums)






