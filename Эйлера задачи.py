
Алгоритм бинарного поиска для создания дерево

def algoritm(number=None):
    # ///Модель комментов
    comment = Post.objects.all()

    # /// Представление элементов базы данных в виде чисел
    massive = [int(number.pk) for number in comment]

    # // Нахождение родительских элементов комментарий
    massive_parent = [number for number in massive if Post.objects.get(pk=number).parent is None]

    # // Нахождение всех дочерних элементов комментарий
    massive_child = [number for number in massive if Post.objects.get(pk=number).parent is not None]
    result = []
    for parent in massive_parent:
        result.append(parent)
    for child in massive_child:
        result.append(child)
    answer = []
    s = True
    for j in range(len(result)):
        for parent_child in result:
            if result[j] != parent_child:
                if result[j] == Post.objects.get(pk=parent_child).parent:
                    answer.append(parent_child)
            if s is True:
                answer.append(result[j])
                s = False
        s = True
    delete_objects_db = Post.objects.delete()
    for create_obj in range(len(answer)):
        create = Post.objects.create()
    return answer




# Числа фибоначи
# a = [1, 1]
# for i in range(0, 8):
#     result = a[i] + a[i + 1]
#     a.append(result)
# print(*a)

# перестановка задачи Эйлера
# from itertools import permutations
#
# perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in perm:
#     print(i)


# Задача 1
# Числа, кратные 3 или 5
# def k(n):
#     sm = 0
#     for i in range(n):
#         if i % 5 == 0 or i % 3 == 0:
#             sm += i
#     return sm
#
#
# print(k(int(input())))

# Задача 2
# def fb(n):
#     p = 0
#     result = [0, 1]
#     for i in range(n):
#         result.append(result[p] + result[p + 1])
#         p += 1
#     sm = 0
#     for n in result:
#         if n % 2 == 0:
#             sm += n
#     return sm
#
#
# print(fb(int(input())))


# def f(n):
#     result = [i for i in range(2, n) if i % 2 != 0 if i % 1 == 0 and i % i == 0]
#     print(max(result))
#
#
# f(int(input()))


# задача 3 простые числа
# numb = int(input("Введите целое число: "))
# print("Результат:", end=" ")
# for i in range(numb - 1, 1, -1):
#     if (numb % i == 0):
#         print(i, end=" ")


# свой вариант простые числа
# number = int(input('Введите целое число:'))
# numbers = [i for i in range(2, number + 1)]
# result = []
# for i in numbers:
#     p = 0
#     for n in range(2, i):
#         if i % n == 0:
#             p += 1
#     if p == 0:
#         result.append(i)
#
# print(max(result))





# задача 4


# Задача 5 #Наименьшее кратное
# numbers = [i for i in range(0, int(input()))]
# result = []
# for n in numbers:
#     p = 0
#     for i in range(1, 21):
#         if n % i == 0:
#             p += 1
#     if p == 20:
#         result.append(n)
#         p -= 20
# print(result)



# Задача 6 Разность между суммой квадратов и квадратом суммы 12 + 22 + ... + 102 = 385 (1 + 2 + ... + 10)2 = 552 = 3025
# square1, square2 = 0, 0
# for n1 in range(1, 101):
#     square1 += n1 ** 2
#     square2 += n1
# print((square2 ** 2) - square1)


# Задача 7 10001-ое простое число
# number = int(input('Введите целое число:'))
# numbers = [i for i in range(2, number + 1)]
# result = []
# for i in numbers:
#     p = 0
#     for n in range(2, i):
#         if i % n == 0:
#             p += 1
#     if p == 0:
#         result.append(i)
#
# print(result[10001])


# Задача 8 Наибольшее произведение в последовательности
# sr = '73167176531330624919225119674426574742355349194934\
# 96983520312774506326239578318016984801869478851843\
# 85861560789112949495459501737958331952853208805511\
# 12540698747158523863050715693290963295227443043557\
# 66896648950445244523161731856403098711121722383113\
# 62229893423380308135336276614282806444486645238749\
# 30358907296290491560440772390713810515859307960866\
# 70172427121883998797908792274921901699720888093776\
# 65727333001053367881220235421809751254540594752243\
# 52584907711670556013604839586446706324415722155397\
# 53697817977846174064955149290862569321978468622482\
# 83972241375657056057490261407972968652414535100474\
# 82166370484403199890008895243450658541227588666881\
# 16427171479924442928230863465674813919123162824586\
# 17866458359124566529476545682848912883142607690042\
# 24219022671055626321111109370544217506941658960408\
# 07198403850962455444362981230987879927244284909188\
# 84580156166097919133875499200524063689912560717606\
# 05886116467109405077541002256983155200055935729725\
# 71636269561882670428252483600823257530420752963450'
# numbers = [int(i) for i in sr]
# num, p = 1, 0
# result = []
# for n in numbers:
#     num *= n
#     p += 1
#     if p == 13:
#         result.append(num)
#         p = 0
#         num = 1
# print(max(result))


# numbers = list(map(int, input().split()))
# i = 0
# mx = []
# while i < 2:
#     n = max(numbers)
#     mx.append(n)
#     numbers.remove(n)
#     i += 1
# print(*mx)



# Задача 8 Особая тройка Пифагора
# a, b, c = map(int, input().split())
# print(a + b + c == 1000)



# Задача 9 Сумма простых чисел
# number = int(input('Введите целое число:'))
# numbers = [i for i in range(2, number + 1)]
# result = []
# for i in numbers:
#     p = 0
#     for n in range(2, i):
#         if i % n == 0:
#             p += 1
#     if p == 0:
#         result.append(i)
#
# print(sum(result))


# Задача 10 Наибольшее произведение в таблице
# box = []
# n = 0
# for i in range(1, int(input()) + 1):
#     n += i
#     box.append(n)
# result = [[] for _ in range(len(box))]
# for j in box:
#     p = 0
#     for s in range(1, n + 1):
#         if j % s == 0:
#             result[p].append(s)
#     if p == 0:
#         p += 1
# print(box)


# Задача 12 Треугольное число с большим количеством делителей
# box = []
# result = []
# n = 0
# p = 0
# for i in range(1, 100000):
#     n += i
#     box.append(i)
#     result.append([])
#     for num in range(1, n + 1):
#         if n % num == 0:
#             result[p].append(num)
#     p += 1
# for i in result:
#     if len(i) == 500:
#         print(i[-1])
#         break
#     else:
#         print('no')






# Задача 13 Большая сумма
# with open('13.txt', 'r') as f:
#     n = 0
#     f = f.read().split()
#     ln = len(f) // 10
#     box = []
#     p = 0
#     res = 0
#     for n in f:
#         if p < 10:
#             res += int(n)
#             box.append(res)
#             p += 1
#         p -= 10
#         res -= res
# print(max(box))


# Задача 14 Пути через таблицу
# numbers = int(input())
# print(numbers * 6)


# Задача 16 Сумма цифр степени
# number = int(input())
# num = str(number ** 1000)
# result = 0
# for i in num:
#     result += int(i)
# print(result)


# Задача 18 Максимальная сумма пути 1(15)

# with open('18.txt', 'r') as f:
#     numbers = f.read().split()
#     numbers = [int(i) for i in numbers]
#     box = [[0] * i for i in range(1, 16)]
#     p = 0
#     n = 0
#     result = []
#     for i in box:
#         result.append([])
#         for j in range(len(i)):
#             result[p].append(numbers[n])
#             n += 1
#         p += 1
#     sm = []
#     for s in result:
#         sm.append(max(s))
#     print(sum(sm))



# Задача 19 Считаем воскресенья(16)
# import datetime
# year = 1901
# day = 1
# month = 0
# rg = 12 * 10
# sm = 0
# for i in range(10):
#     for j in range(12):
#         month += 1
#         rs = datetime.date(year, month, day)
#         res = rs.strftime('%A')
#         if res == 'Wednesday':
#             sm += 1
#
#     month -= 12
#     year += 1
# print(sm)

# Задача 20 Сумма цифр факториала
# numbers = int(input())
# s = 1
# for i in range(1, numbers):
#     s *= i
# result = 0
# for st in str(s):
#     result += int(st)
# print(result)



# Задача 21 Дружественные числа
# numbers = [i for i in range(1, int(input()))]
# for n in numbers:
#     number = n
#     sm = 0
#     p = 0
#     for i in range(1, number):
#         if number % i == 0:
#             sm += i
#     for s in range(1, sm):
#         if sm % s == 0:
#             p += s
#     if p == number:
#         print(sm, p)

# Задача 22 Очки за имена
# with open('names.txt', 'r', encoding='utf8') as f:
#     box = []
#     for n in f.read().rsplit('",'):
#         s = n.lstrip('",')
#         box.append(*s.split())
#     alp = 'ABCDEFJGHIJKLMNOPQRSTUVWXWZ'
#     box = sorted(box)
#     sum_file_points = 0
#     for i in box:
#         st = i
#         i_name = int(box.index(st) + 1)
#         i_letters = 0
#         for s in st:
#             for s_a in alp:
#                 if s == s_a:
#                     i_letters += int(alp.index(s) + 1)
#         sum_file_points += (int(i_name * i_letters))
#     print(sum_file_points)


# number = int(input())
# s_u_m_a = 0
# for i in range(1, number + 1):
#     if i % 2 == 0:
#         sm = 0
#         for i_d in range(1, i):
#             if i % i_d == 0:
#                 sm += i_d
#         if sm == i:
#             s_u_m_a += sm
#             print(sm)
# print(s_u_m_a)


# numbers = list(input().split())
# l_n = len(set(numbers))
# l_e_n = (l_n * (l_n - 1) * (l_n - 2))
# i = 0
# n = 0
# result = []
# while i < l_e_n * 10:
#     if n != l_n - 1:
#         numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]
#         result.append(''.join(numbers))
#         i += 1
#         n += 1
#     else:
#         n -= l_n + 1
#         numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]
#         result.append(''.join(numbers))
#         i += 1
#         n += 1
# print(len(set(result)))

# import itertools
# print(*itertools.permutations([0, 1, 2]),sep='\n')




# Задача 26 1000-Значное число Фибоначчи
# result = [1, 1]
# i = 0
# for _ in range(100000):
#     sm = result[i] + result[i + 1]
#     result.append(sm)
#     i += 1
#     if len(str(sm)) == 1000:
#         print('F-' + str(result.index(sm) + 1))
#         break
#




# Задача 26
# from collections import Counter
# # for i in range(1, 10):
# #     dr = [1 % i]
# #     d_st = set(list(str(dr)))
# n = [1,2,3, 1]
# p = 1
# print(Counter(n).values())



