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


class Person:  # создание класса
    def say(self, message):  # создание метода который имеет ссылку на объекты(self ) и параметр message
        print(message)

    def say_hello(self):    # создание второго метода класса  с ссылкой на объект (self)
        self.say("I like u")  # обращение к первому метода класса который выводит инфу


text = Person()  # создание переменно и присвоение ей объекта класса
text.say_hello()  # обращение объекта класса к методу класса
text.say(message="i dont like u")  # обращение к методу класса который имеет доп параметр