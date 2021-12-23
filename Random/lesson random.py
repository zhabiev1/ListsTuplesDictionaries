# import random  # импорт библиотека random

# print(random.randint(-1000, 1000))  # генерация рандомного числа от мин до максимального


# print(random.randrange(10))  # рандомное число от 0 до 9
# print(random.randrange(5, 10))  # рандомное число от 5 до 9

# print(random.random())  # метод библиотеки для генерации значений от 0 до 1

# a = random.random()  # метод библиотеки для генерации значений от 0 до 10
# print(a)
# b = round(a, 4)  #  функция выводит числа после запятой
# print(b)

# a = round(random.random(), 4)  # выводит рандомное число от 0 до 1 обрезанные до 4 после запятой
# print(a)

# a = random.random() * 10  # выводит рандомные значения умноженные на 10
# print(a)

# import random
# a = random.randrange(0, 1001)
# print(a)
# if a % 2 != 0:
#     print("Извините.но вы проиграли")
# if a % 2 == 0:
#     print("Вы выиграли")


# def casino(ran):
#     if ran % 2 != 0:
#         print("Вы проиграли")
#     if ran % 2 == 0:
#         print("Вы выиграли")
#
#
# casino(a)