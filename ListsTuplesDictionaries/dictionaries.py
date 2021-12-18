# a = {  # создаём dictionary
#     1: "Maga",  # вводим значения dictionary
#     2: "Dima",  # вводим значения dictionary
#     3: "Sergey"  # вводим значения dictionary
# }  # закрываем dictionary

# print(a)

# country = {  # создаём dictionary
#     "USA": "Washington",  # вводим значения dictionary
#     "Spain": "Madrid",  # вводим значения dictionary
#     "Ukraine": "Kiev"  # вводим значения dictionary
# }  # закрываем dictionary

# print(country)

# objects = {}  # создаём пустой dictionary
# objects2 = dict()  # второй способ,чтобы создать dictionary
# print(objects)
# print(objects2)

# users_list = [  # создаём лист
#     [38098560917, "Maga"],  # создаём лист в листе и заполняем элементами
#     [380684507689, "Sergey"], # создаём лист в листе и заполняем элементами
#     [38098678390, "Dima"]  # создаём лист в литсе и заполняем элементами
# ]  # закрываем лист
# print(users_list)
# users_dict = dict(users_list)  # изменяем тип данных на dictionary
# print(users_dict)

# users_list = (  # создаём кортеж
#     (38098560917, "Maga"),  # создаём кортеж в кортеже и наполняем данными
#     (380684507689, "Sergey"),  # создаём кортеж в кортеже и наполняем данными
#     (38098678390, "Dima")  # создаём кортеж в кортеже и наполняем  данными
# )  # закрываем кортеж
# print(users_list)
# users_dict = dict(users_list)  # меняем тип данных кортеж на dictionary
# print(users_dict)

# country = {  # создаём dictionary
#     "USA": "Washington",  # наполняем его данными
#     "Spain": "Madrid",  # наполняем его данными
#     "Ukraine": "Kiev"  # наполняем его данными
# }  # закрываем dictionary
# print(country["Ukraine"])  # выводит значение по ключу
# country["Ukraine"] = "Lviv"  #  меняет значение ключа Ukraine на Lviv
# print(country["Spain"])  # выводит значение по ключу
# country["Spain"] = "Barcelona"  # меняет значение ключа Spain на Barcelona
# print(country)