# numbers = [1, 2, 3, 4, 5]  # создаём лист элементов из чисел
# people = ["Kate", "Maga"]  # создаем лист из строк
# a = []  # создаем  пустой лист
# a1 = list()   # создаем лист с помощью функции
# objects = ["Maga", 3.5, True, 1]  # создаем лист элементов разных типа данных
# print(objects)


# number = [1, 2, 3, 4, 5] # создаем лист элементов инт
# number_2 = list(number)   # создаем переменную и делаем копию лист с помощью функции лист
# print(number)
# print(number_2)


# a = list("Maga")  #  создаем лист с помощью функции
# print(a)

# b = ["Maga"]  # создаем лист
# print(b)


# a = [4] * 20   # дублирование листа
# print(a)

# people = ["Maga", "Dima", "Max", "Stefan", "Kirill"] # создаем  лист
# print(people[-1])  # последний индекс


# people = ["Maga", "Dima", "Max", "Stefan", "Kirill"]  # создаем лист
# people[0] = True  # замена элемента в листе по индексу
# print(people)


# numbers = [1, 2, 3]  # создаем лист
# num_1, num_2, num_3 = numbers  # разбивание листа на отдельные переменные
# print(num_1)
# print(num_2)
# print(num_3)

# people = ["Maga", "Dima", "Max", "Stefan", "Kirill"]  # cоздаем лист
# for i in people:  # прогон листа
#     print(i)  # вывод отдельных элементов листа

# number_1 = [1, 2, 3]  # cоздаем лист
# number_2 = [1, 2, 3]  # cоздаем лист
# if number_1 == number_2: # сравнивание двух листов
#     print("списки равны")
# else:  # иначе
#     print("списки не равны")

# people = ["Maga", "Dima"]  # cоздаем лист
# print(people)
# people.append("Max")  # добавляем элемент в конец листа
# print(people)
# people.insert(1, "Stefan")  # добавляет элемент в лист по индексу
# print(people)
# people.extend(["Lukas", "Kai"])  # добавляет группу элементов в конец листа
# print(people)
# index = people.index("Maga")  # определяет индекс элемента в листе
# print(index)
# people.pop(-1)  # удаляет по индексу
# print(people)
# people.remove("Max")  # удаляет элемент по значению
# print(people)
# people.clear()  # очищает лист
# print(people)


# people = ["Max", "Stefan", "Kirill"]  # cоздаем лист
# question = input("Введите имя: ")  # принимаем от пользователя значение
# if question in people:  # если значение есть в списке то выводит
#     print("Найдено")
# else:  # если нет то
#     print("пользователь не найден")


# people = ["Maga", "Dima", "Max"]  # cоздаем лист
# del people[-1]  # удаление с помощью оператора
# print(people)


# numbers = [10, 9, 5, 6, 3, 4]   # cоздаем лист
# numbers.sort()  # сортируем методом
# print(numbers)
# numbers.reverse()  # разворачиваем лист задом на перед
# print(numbers)

# numbers = [1, 5, 4.5, 6, 3, 2]  # cоздаем лист
# print(sorted(numbers))  # сортируем с помощью функции sorted
# print(len(numbers))  # измеряем лист
# print(min(numbers))  # минимальное значение
# print(max(numbers))  # максимальное значение


# people_1 = ["Maga", "Dima", "Max"]  # cоздаем лист
# people_2 = people_1  # создание копии листа
# print(people_1)
# print(people_2)
# people_2.append("Martin")  # добавляем в конец новый элемент
# print(people_1)
# print(people_2)


# list_1 = ["Max", "Alex", "Kate"]  # cоздаем лист
# list_2 = list_1.copy()  # копируем лист для редактирования
# print(list_1)
# print(list_2)
# list_2.append("Natalie")  # добавляем ко второй копии новый элемент
# print(list_1)
# print(list_2)


# people = ["Maga", "Dima", "Max", "Stefan", "Kirill"]  # cоздаем лист
# print(people[:3])  # показывает до 3 элемента
# print(people[1:3])  # показывает от 1до 3
# print(people[1:5:2])  # показывает от  1 до 5 через 2

# people = [  # создаем лист
#     ["Maga", 21],
#     ["Alex", 22],
#     ["Dima", 25],
#     ["Kai", 26]
# ]
# print(people)
# print(people[0])  # выводит элемент  листа по индексу
# print(people[0][0]) # выводит элемент подлиста по индексу


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# question = int(input("Введите число которое хотите найти"))
# if question in numbers:
#     print("Такое число есть")
# else:
#     print("Такого числа нет")

# list_1 = [5, 4, 65, 6, 7, 8, 9]
# list_1.reverse()
# print(list_1)


def change(lst):
    print(lst)
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)

change([1, 2, 3, 4, 5])
