# x = int(input("Cколько часов спит Тимофей ночью?"))
# y = int(input("Cколько минут спит Тимофей днём?"))
# print((x * 60) + y)

# x = int(input("Сколько минут нужно спать Коле?"))
# print(x / 60)
# print(x % 60)


# a = int(input("Cколько часов рекомендуется спать Ане?"))
# b = int(input("Сколько часов нельзя спать  Ане ?"))
# h = int(input("Cколько Аня спит сейчас ?"))
#
# if h > b:
#     print("Это пересып")
# elif h >= a and h <= b:
#     print("Это норма")
# elif h < a:
#     print("Это недосып")

# from math import sqrt

# a = int(input("Введите число а :"))
# b = int(input("Введите число b :"))
# c = int(input("Введите число c :"))
# p = ((a + b + c) / 2)
# s = sqrt(p * (p - a) * (p - b) * (p - c))
# print(s)

# a = int(input("Введите число а: "))
#
# if a > -15 and  a <= 12 or a > 14 and a < 17 or a >= 19:
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
#     elif operation == "mod":
#         print(a % b)
#     elif operation == "pow":
#         print(a ** b)
#     elif operation == "div":
#         print(a // b)
# except ZeroDivisionError:
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
# print(calculator.get(operation, "такого знака не существует"))

# from math import sqrt
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
#     s = PI * pow(r, 2)
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
# a = sorted(numbers)
# print(a)
# print(a[2])
# print(a[0])
# print(a[1])

# lucky_ticket = input("Введите номер билета: ")
# lucky_list = []
#
# for i in lucky_ticket:
#     lucky_list.append(i)
# print(lucky_list)
#
# s1 = 0
# s2 = 0
#
# for i in lucky_list[0:3]:
#     s1 += int(i)
# for i in lucky_list[3:6]:
#     s2 += int(i)
# print(s1)
# print(s2)
#
# if s1 == s2:
#     print("У тебя счастливый билет!")
# else:
#     print("У тебя не счастливый билет")

# check_the_name = input("Введите имя: ")
# check_the_age = input("Введите возраст: ")
# print(f"Привет, {check_the_name}. тебе,{check_the_age}")

# a = f"{2 * 25}"
# b = 2 * 25
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# name = input("Введите ваше имя:")
# profession = input("Введите вашу проффесию")
# married = input("Женаты ли вы?")
# info = (
#     f"привет, {name}"
#     f" ваша проффесия:{profession}"
#     f" Вы:{married}"
#
# )
# print(info)

# b = 0
# while True:
#     a = int(input("Введите числа: "))
#     if a == 0:
#         break
#     else:
#         b += a
# print(b)

# while True:
#     a = int(input("Введите число: "))
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     else:
#         print(a)
#         continue

# counter = []
# a = int(input("Введите число а: "))
# b = int(input("Введите число b: "))
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         counter.append(i)
# print(counter)
# c = 0
# for i in counter:
#     c += i
# print(c / len(counter))

# gc = input("Введите GC cостав: ")
# sum = ""
# for i in gc:
#     if i == "c" or i == "C":
#         sum += i
#     if i == "g" or i == "G":
#         sum += i
# print(len(sum) / len(gc) * 100)

sum = 0  # вводим переменную для суммы
pow_finally = 0  # вводим переменную для квадрата

while True:  # цикл для повтора
    numbers = int(input("Введите число: "))  # пользователь вводит цифры
    sum += numbers  # в переменную добавляется числа
    pow_finally += pow(numbers, 2)  # все добавленные числа возносятся в степень
    if sum == 0:  # если сумма равна 0
        break  # то прекращается и выводит сумму всех чисел в квадрате
print(pow_finally)



