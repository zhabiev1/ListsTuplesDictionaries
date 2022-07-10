# class Person:  # стандартное создание класса
#     pass   #  использование оператора затычки
#
#
# object_1 = Person()  # создание объекта класса
# object_2 = Person()  # создание объекта класса

# для создания объекта класса применяется конструктор(если он не переопределен - используется стандартный конструктор)


# class Person:  # создание класса
#     def say_hello(self):  # создание метода который имеет ссылку на объект(self)
#         print("hello")
#
#
# object_1 = Person()  # создание объекта класса и присвоение к переменной
# object_1.say_hello()  # обращение объекта класса к методу класса


# class Person:  # cоздание класса
#     def say(self, message):  # создание метода класса с ссылкой на объект и вторым параметром message
#         print(message)
#
#
# user = Person()  # создание объекта и присвоение к переменной
# user.say(message="you are smart")   # обращение объекта класса к методу класса в котором передается параметр


# class Person:  # создание класса
#     def say(self, message):  # создание метода который имеет ссылку на объекты(self ) и параметр message
#         print(message)
#
#     def say_hello(self):    # создание второго метода класса  с ссылкой на объект (self)
#         self.say("I like u")  # обращение к первому метода класса который выводит инфу
#
#
# text = Person()  # создание переменно и присвоение ей объекта класса
# text.say_hello()  # обращение объекта класса к методу класса
# text.say(message="i dont like u")  # обращение к методу класса который имеет доп параметр


# class Person:  # создание класса
#     def __init__(self):  # создание метода- конструктора(который выполняется при создании объекта)
#         print("Создание объекта person")
#
#     def say_hello(self):  # создание метода класса
#         print("Hello")
#
#
# a = Person()
# a.say_hello()


# class Person:  # создание класса
#     def __init__(self, name):  # определение конструктора класса с дополнительным параметром name
#         self.name = name  # создание атрибута класса и присовение ему параметра
#         self.age = 1  # создание атрибута класса и приавосение ему значение по стандарту
#
#
# a = Person("Maga")  # создание объекта класса
# print(a.name)  # вывод атрибута класса
# print(a.age)  # вывод атрибута класса
# a.age = 21  # изменение атрибута класса
# print(a.age)  # вывод атрибута класса
# a.company = "microsoft"  # создание диномического аттрибута класса
# print(a.company)  # вывод атрибута класса


# class Person:  # создание класса
#     def __init__(self, name, age):  определение конструктора класса с двумя параметрами
#         self.name = name  # создание атрибута класса
#         self.age = age  # создание атрибута класса
#
#     def display_info(self):  # создание метода класса
#         print(f"Name: {self.name} Age: {self.age}")  # вывод атрибута класса с помощью f{}


# a = Person("Maga", 23)  # создание объекта класса
# a.display_info()  # вызов метода класса
# a.name = "Dima"  # изменение атрибута класса
# a.age = 24  # изменение атрибута класса
# a.display_info()  # вызов метода класса


# class Person:  # создание класса
#     def __init__(self, name, age):  # опредение конструктора класса с двумя параметрами
#         self.name = name  # создание атрибута
#         self.age = age  # создание атрибута
#
#     def display_info(self):  # создание метода класса
#         print(f"Name: {self.name} Age: {self.age}")  # вывод атрибутов  с помощью  f{}


# object1 = Person("Maga", 23)
# object2 = Person("Alex", 24)
# object3 = Person("Max", 25)
# object4 = Person("Kai", 26)
# object5 = Person("Lukas", 27)


# object1.display_info()
# object2.display_info()
# object3.display_info()
# object4.display_info()
# object5.display_info()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(f"Name: {self.name} Age: {self.age}")
#
#
# a = Person("Maga", 23)
# a.display_info()
# a.age = -10
# a.display_info()


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def check_age(self, age):
        if 90 >= age > 1:
            self.__age = age
        else:
            print("Dont allowed age")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"name: {self.__name}, age: {self.__age}")


object_of_data = Person("Maga", 23)
object_of_data.display_info()
object_of_data.check_age(-25)
object_of_data.display_info()





