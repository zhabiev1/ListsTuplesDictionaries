# class Person:  # создаём класс
#     name = "Maga"  # cоздаём атрибут
#     age = 22  # создаём атрибут
#
#     def display_indo(self):  # метод класса
#         print("Привет, меня зовут", self.name, "мне", self.age, "лет")  # self обращаемся к атрибутам
#
#
# person_one = Person()  # создаём объкт класса персон
# person_one.display_indo()  # вызываем метод класса для объекта

# class Person:  # создаём класс
#     def __init__(self, name, age):  # создаём конструктор
#         self.name = name  # создаём атрибут
#         self.age = age  # создаём атрибут
#
#     def display_info(self):  # создаём метод класса
#         print("Привет,меня зовут", self.name, "мне", self.age, "года")  # обращаемся с помощью self к атрибутам
#
#
# person_one = Person("Maga", 22)  # создаём  объект класса для персон
# person_one.display_info()  # вызываем метод класса для объекта
# person_two = Person("Cергей", 22)  # создаём новый объект класса
# person_two.display_info()  # вызываем метод класса для объекта

# class Person:  # создаём класс
#     def __init__(self, name):  # создаём конструктор
#         self.name = name  # создаём атрибут
#
#     def __del__(self):  # создаём деструктор
#         print(self.name, "deleted from memory")  # удаляем атрибут из памяти
#
#     def display_info(self):  # создаём метод для объекта
#         print("Привет,меня зовут", self.name)  # self обращается к атрибутам
#
#
# person_one = Person("Maga")  # создаём объект класса пермон
# person_one.display_info()  # вызываем метод класса для объекта
# del person_one  # удаляем атрибут





