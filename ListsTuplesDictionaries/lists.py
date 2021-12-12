# numbers = [1, 2, 3, 4, 5]  # мы создаём лист и наполняем его элементами

# numbers1 = []  # мы создаём пустой лист
# numbers2 = list() # редкое написание (создание листа как и на 3 строке)

# numbers = [1, 2, 3, 4, 5] # мы создаём лист и наполняем его элементами
# numbers2 = list(numbers)  # создаём лист и вводим в него значения другого листа
# numbers3 = numbers  # создаём лист и вводим в него значения другого листа
# print(numbers)
# print(numbers2)
# print(numbers3)
# numbers = [1, 2, 3, 4, 5]  # создаём лист
# print(numbers[0])
# print(numbers[2])
# print(numbers[4])
#
# test = ["mouse", 3.0, True, 3, ["Cat", 4.0, False, 2], []]  # создаём лист и наполняем его значениями разных типов
# print(test[2])
# print(test[3])
# print(test[5])
#
# numbers[0] = 10  #  меняем значение по индексу в листе
# print(numbers[0])
#
# test[2] = False # меняем значение по индексу в литсе
# test[5] = 1  # меняем значение по индексу в листе
# print(test)

# numbers = [5] * 6  # создаём лист и дублируем его значение 6 раз
# print(numbers)

# numbers = list(range(10))  # создаём лист и записываем в него значения от 0 до 9
# print(numbers)

# number = list(range(3, 10))  # создаём лист и записывем в него значения от 3 до 9
# print(number)

# number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # создаём лист и записываем в него значения от 1 до 9
# number2 = list(range(1, 10))  # создаём лист и записываем в него значения от 0 до 9
# print(number1)
# print(number2)

# objects = [1, 2.0, True, "Space", []]  # создаём лист и записываем все типы данных,которые мы знаем
# for i in objects:  # цикл, который перебирает элементы листа
#     print(i)


# objects = [2, 3.0, False, "Phone", []]  # создаём лист и записываем в него типы данных,которые мы знаем
# i = 0  # переменная для того,чтобы задать счётчик для цикла while
# while i < len(objects):  # цикл делает тоже самое,что и for i in
#     print(objects[i])
#     i += 1  # увеличиваем на 1


# a = [1, 5, 10] # создаём лист с значениями инт
# print(a)
# a.append("Maga")  # метом,который добавляет элемент в конец листа
# print(a)
# a.reverse()  # метод, который возвращает обратный лист
# print(a)
# a.clear()  # метод,который опустошает лист
# print(a)

# numbers = [1, 3, 8, 6, 1, 9, 4]  # создаём лист с интовыми элементами
# print(len(numbers))  # функций len,которая считает кол-во элементов
# print(numbers)
# print(sorted(numbers))  # функция sorted,чтобы отсортировать по возрастанию
# print(min(numbers))  # функция для минимального часа
# print(max(numbers))  # функция для максимально числа


# users = ["Maga", "Max"]  # создаём лист и наполняем его элементами
# users.append("Sergey")  # добавляем новый элемент в лист в конец
# print(users)
# users.insert(0, "John")  # добавляем элемент по индексу
# print(users)
# print(users.index("Maga"))
# users.pop(1)  # удаляем элемент по индексу
# print(users)
# users.clear()  # очищаем лист
# print(users)

# delete_city = input("Введите город,который Вы хотите удалить")  # принмаем от пользователя город
# city = ["New York", "Munich", "Tokyo", "Madrid", "Moscow"]
# print(city)
# if delete_city in city:
#     city.remove(delete_city)
# print(city)

# delete_city = input("Введите город,который Вы хотите удалить")
#
#
# def check_and_delete(city):
#     list_city = ["New York", "Munich", "Tokyo", "Madrid", "Moscow"]
#     if city in list_city:
#         index = list_city.index(city)
#         list_city.pop(index)
#         return list_city
#
#
# print(check_and_delete(delete_city))

# name = input("Введите имя: ")
#
# users = ["John", "John", "Maga", "Dima", "Maga", "John"]
# print(users.count(name))

# user_name = input("Введите имя: ")
#
#
# def counter_users(name):
#     name_check = ["John", "John", "Maga", "Dima", "Maga", "John"]
#     return name_check.count(name)
#
#
# print(counter_users(user_name))





