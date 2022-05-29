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


# def change(lst):
#     print(lst)
#     lst[0], lst[-1] = lst[-1], lst[0]
#     print(lst)
#
# change([1, 2, 3, 4, 5])

# person = ("Maga", 21)
# print(person)

# person = "Maga", 21
# print(person)

# person = ("Maga",)
# print(person)
# print(type(person))

# object_1 = ["Maga", 23, "Germany"]
# object_2 = tuple(object_1)
# print(object_2)

# object_1 = ["Maga", 23, "Munich"]
# print(tuple(object_1))

# people = ("Maga", "Kris", "Marie", 23, 22, 1998)
# print(len(people))

# cities = ("Munich", "Kiew", 2022, True, 4.5)
# print(cities[-1])

# a = (True, "maga", 23, 4004, 4.5, False)
# print(a[:3])
# print(a[2:5])

# b = ("Maga", True, False, 4.5, 5.6, "Alex", "Park", 2.5, "Tea", " Bed", "short")
# print(b[1:6])
# print(b[8:11])
# print(b[-1])
# print(b[:5])

# def get_user():
#     name = "Maga"
#     age = 23
#     company = "Apple"
#     return name, age, company


# print(get_user())

# stuff = (False, True, "key", "cellphone", "charger", 1)
# for i in stuff:
#     print(i)

# a = (False, True, "Maga", 23,)
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# users = ("Maga", "Alex", "Dima", "Natali", "Kai")
# question = input("Give your name")
# if question in users:
#     print("user is in list of elements")
# else:
#     print("nit fined")

# users = {
#     0: "Maga",
#     1: "Dima",
#     2: "Kai",
#     3: "Max",
#     4: "Kate"
# }
# print(users)

#
# car = {
#     "Mercedes": "W220",
#     "BMW": "x5",
#     "Ferari": "6786",
#     "Toyota": "Landkruser"
# }
# print(car)

# empty = {
#
# }
# print(empty)
#
#
# empty_1 = dict()
# print(empty_1)

# user_list = [
#     [1, "Maga"],
#     [2, "Alex"],
#     [3, "Kai"],
#     [4, "Kate"]
# ]
# print(user_list)
#
# user_dictionary = dict(user_list)
# print(user_dictionary)


# user_tuple = (
#     ("Germany", "Berlin"),
#     ("UK", "London"),
#     ("Spain", "Madrid"),
#     ("Italy", "Milan")
# )
# print(user_tuple)
# user_dictionary = dict(user_tuple)
# print(user_dictionary)


# books = {
#     "Bulgakov": "Master and Margaret",
#     "Erich Remarque": "Three friends",
#     "Agatha Christie": "The Mousetrap",
#     "Adolf Hitler": "Mein Kampf",
#     "Arthur Doile": "Sherlock Holmes"
# }
# print(books)
# print(books["Bulgakov"])
# books["Adolf Hitler"] = "Schönheit der Rasse"
# print(books)
# a = books.get("Agatha Christie")
# print(a)
# del books["Adolf Hitler"]
# print(books)
# del books["Arthur Doile"]
# print(books)
# books.pop("Bulgakov")
# print(books)


# users = {
#     1: "Munich",
#     2: "Kyiv",
#     3: "Lemberg"
# }
# print(users)
# user_finally = users.copy()
# print(user_finally)
# users.clear()
# print(users)

# users = {
#     1: "Maga",
#     2: "Dima",
#     3: "Kai"
# }

# print(users[1])
# print(users.get(1))
# users.pop(3)
# print(users)
# del users[2]
# print(users)


# users = {
#     "Maga": 31434234,
#     "Alex": 432423423,
#     "Dima": 42342342
# }
# print(users)
# for i in users:
#     print(users[i])


# users = {
#     "Maga": 31434234,
#     "Alex": 432423423,
#     "Dima": 42342342
# }
# for i in users.items():
#     print(i)


# users = {
#     "Maga": 31434234,
#     "Alex": 432423423,
#     "Dima": 42342342
# }
# for i in users.keys():
#     print(i)


# users = {
#     "Maga": 31434234,
#     "Alex": 432423423,
#     "Dima": 42342342
# }
# for i in users.values():
#     print(i)


# users = {
#     "Maga": {
#         "Phone": "65667676",
#         "Email": "ksdjfksdf@gmail.com"
#     },
#     "Dima": {
#         "Phone": "34234223",
#         "Email": "ddafsdf@yahoo.com"
#     },
#     "Max": {
#         "Phone": "4234234234",
#         "Email": "dasdsdad@yahoo.com"
#     }
# }
# print(users)
# print(users["Maga"]["Phone"])
# print(users["Max"]["Email"])

# users = {"Maga", "Jonas", "Wolfgang", "Joachim", "Kai"} # создаем сет
# print(users)
# users = {"Maga", "Jonas", "Joachim", "Maga"} # создаем сет
# print(users)

# numbers = {1, 2, 3, 4, 5, 6, 7, 11, 9, 10} # создаем числовой сет который сортирует числа
# print(numbers)

# objects = {"Maga", True, 10000, ("Maga", "Kai"), 4.5}  # создаем сет с разными типами данных
# print(objects)
# print(len(objects))   # выводим длину сета


# objects = {"Maga", True, 10000, ("Maga", "Kai"), 4.5}  # создаем сет с разными типами данных
# objects.add("False")  # добавляем новый элемент в сет
# print(objects)


# objects = {"Maga", True, 10000, ("Maga", "Kai"), 4.5}  # создаем сет с разными типами данных
# objects.remove(4.5)  # удаляет элемент
# print(objects)
# objects.discard(("Maga", "Kai"))  ]  # удаляет элемент(лучше потому что не выводит ошибку а предупреждение если элемент не найден
# print(objects)
# objects.clear()  # полностью очищает сет
# print(objects)


# objects = {"Maga", True, 10000, ("Maga", "Kai"), 4.5}  # создаем сет с разными типпами данных
# for i in objects:  # прогон элементов в сете
#     print(i)

# users = frozenset({"Maga", "Dima", "Kai", "Kate"}) # неизменяемый сет (frozenset)
# print(users)
# print(type(users))

