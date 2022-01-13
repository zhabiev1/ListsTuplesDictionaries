# x = int(input("Cколько часов спит Тимофей ночью?"))  # принимаем значение кол-ва сна
# y = int(input("Cколько минут спит Тимофей днём?"))  # принимаем значение кол-ва сна
# print((x * 60) + y)  # конвертируем в минуты и высчитываем бщее время в минутах

# x = int(input("Сколько минут нужно спать Коле?"))  # принимаем значение кол-ва сна
# print(x / 60)  # конвертируем часы в минуты
# print(x % 60)  # высчитываем минуты


# a = int(input("Cколько часов рекомендуется спать Ане?"))
# b = int(input("Сколько часов нельзя спать  Ане ?"))
# h = int(input("Cколько Аня спит сейчас ?"))
#
# if h > b:   # если кол-ва сна Ани больше нормы
#     print("Это пересып")
# elif h >= a and h <= b:  # если кол-во сна Ани больше рекомендаций и меньше пересыпа
#     print("Это норма")
# elif h < a:  # если кол-ва сна меньше рекомендаций
#     print("Это недосып")

# from math import sqrt  # импортируем функцию коренька квадрата

# a = int(input("Введите число а :"))
# b = int(input("Введите число b :"))
# c = int(input("Введите число c :"))
# p = ((a + b + c) / 2)
# s = sqrt(p * (p - a) * (p - b) * (p - c))  # вычисление по формуле Гирона
# print(s)

# a = int(input("Введите число а: "))  # принимаем значение от пользователя
#
# if a > -15 and  a <= 12 or a > 14 and a < 17 or a >= 19:  # проверяли число на наличие числа в промежутке
#     print(True)
# else:
#     print(False)

# a = float(input("Введите число а: "))
# b = float(input("Введите число b: "))
# operation = input("Введите операцию:(+, -, /, *, mod, pow, div) ")
#
# try:
#     if operation == "+":
#         print(a + b)
#     elif operation == "-":
#         print(a - b)
#     elif operation == "*":
#         print(a * b)
#     elif operation == "/":
#         print(a / b)
#     elif operation == "mod":  #  % остаток
#         print(a % b)
#     elif operation == "pow":  #  в квадрате **
#         print(a ** b)
#     elif operation == "div":  #  деление на цело //
#         print(a // b)
# except ZeroDivisionError:  # если деление на ноль,то напишет "деление на ноль" вместо ошибки
#     print("Деление на ноль!")


# a = float(input("Введите число а: "))
# b = float(input("Введите число b: "))
# operation = input("Введите операцию:(+, -, /, *, mod, pow, div) ")
# calculator = {
#     "+": a + b,
#     "-": a - b,
#     "*": a * b,
#     "/": a / b,
#     "mod": a % b,
#     "pow": a ** b,
#     "div": a // b
# }
# print(calculator.get(operation, "такого знака не существует"))  # функция get вызывает ключи словаря

# from math import sqrt  # библиотека мат для корня квадрата
# PI = 3.14
# form_of_the_rooms = input("Ввведите форму комнаты:(треугольная,прямоугольная,"
#                           "круг ")
# if form_of_the_rooms == "треугольная":
#     a = float(input("Введите первое число: "))
#     b = float(input("Введите второе число: "))
#     c = float(input("Введите третье число: "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь треугольника равна:", s)
# elif form_of_the_rooms == "круг":
#     r = float(input("Введите радиус круга: "))
#     s = PI * pow(r, 2)  # pow возведение в степень
#     print("Площадь круга равна : ", s)
# elif form_of_the_rooms == "прямоугольная":
#     a = float(input("Введите первую  сторону: "))
#     b = float(input("Введите вторуб сторону: "))
#     s = a * b
#     print("Площадь прямоугольника равна: ", s)


# a = int(input("Введите число а : "))
# b = int(input("Введите число b : "))
# c = int(input("Введите число c : "))
#
# numbers = [a, b, c]
# a = sorted(numbers)  # сортируем лист от меньшего к большему
# print(a)
# print(a[2])
# print(a[0])
# print(a[1])

# lucky_ticket = input("Введите номер билета: ")
# lucky_list = []  # создание пустого листа
#
# for i in lucky_ticket:
#     lucky_list.append(i)  # append добавляет в конец элемент
# print(lucky_list)
#
# s1 = 0
# s2 = 0
#
# for i in lucky_list[0:3]:  # создаём цикл for  и прогоняем данные от 0 до 3
#     s1 += int(i)  # добавляем в переменную S1
# for i in lucky_list[3:6]:  #  прогоняем данные от 3 до 6
#     s2 += int(i)  # добавляем в переменную s1
# print(s1)
# print(s2)
#
# if s1 == s2:  # условие при котором s1 == s2
#     print("У тебя счастливый билет!")
# else:  #  в другом случае
#     print("У тебя не счастливый билет")

# check_the_name = input("Введите имя: ")
# check_the_age = input("Введите возраст: ")
# print(f"Привет, {check_the_name}. тебе,{check_the_age}")  # f принимает значение str

# a = f"{2 * 25}"  # выдаёт строку
# b = 2 * 25  # int
# print(a)
# print(b)
# print(type(a))  # type чтобы узнать тип
# print(type(b))

# name = input("Введите ваше имя:")
# profession = input("Введите вашу проффесию")
# married = input("Женаты ли вы?")
# info = (  # создание кортежа
#     f"привет, {name}"  # обработка строки f str
#     f" ваша проффесия:{profession}"
#     f" Вы:{married}"
#
# )
# print(info)

# b = 0
# while True:  # цикл чтобы спрашивало несколько раз
#     a = int(input("Введите числа: "))
#     if a == 0:
#         break  # останавливает программу
#     else:
#         b += a  # добавляет число в переменную
# print(b)

# while True:
#     a = int(input("Введите число: "))
#     if a < 10:
#         continue  # переход на новую итерацию цикла
#     elif a > 100:
#         break
#     else:
#         print(a)
#         continue

# counter = []
# a = int(input("Введите число а: "))
# b = int(input("Введите число b: "))
# for i in range(a, b + 1):  # лист элементов  от и до
#     if i % 3 == 0:  # если число нацело делится на 3
#         counter.append(i)  # добавляем в  конец листа
# print(counter)
# c = 0
# for i in counter:
#     c += i
# print(c / len(counter))  #

# gc = input("Введите GC cостав: ")
# sum = ""
# for i in gc:
#     if i == "c" or i == "C":
#         sum += i
#     if i == "g" or i == "G":
#         sum += i
# print(len(sum) / len(gc) * 100)

# sum = 0  # вводим переменную для суммы
# pow_finally = 0  # вводим переменную для квадрата
#
# while True:  # цикл для повтора
#     numbers = int(input("Введите число: "))  # пользователь вводит цифры
#     sum += numbers  # в переменную добавляется числа
#     pow_finally += pow(numbers, 2)  # все добавленные числа возносятся в степень
#     if sum == 0:  # если сумма равна 0
#         break  # то прекращается и выводит сумму всех чисел в квадрате
# print(pow_finally)

# numbers = float(input("Введите число :"))  # принимаем флоатовое значение

# def f(x):  # создаём функцию
#     if x <= -2:
#         a = 1 - pow((x + 2), 2)  # вводим переменную для того,чтобы могли возвратить
#         return a  # возвращаем а
#     if x > - 2 and x <= 2:
#         b = -(x / 2)
#         return b
#     if x > 2:
#         c = pow((x - 2), 2) + 1
#         return c
#
#
# print(f(numbers))


# import math
#
#
# r = float(input("Введите радиус: "))
# print(2 * math.pi * r)


# import request
# import time
# print(time.time())
# import random
# import numpy


# a = {  # cоздаём dictionary
#     "13": "Maga",
#     "14": "Dima",
#     "15": "Taisa"
# }
# print(len(a))