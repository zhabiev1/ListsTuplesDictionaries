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

# question = input("Введите страну! ") # просим юзера ввести страну
# countries = {  # создаём dictionary
#     "Japan": "Tokyo",  # заполняем значение по ключу
#     "Usa": "Washington",  # заполняем значение по ключу
#     "Spain": "Madrid",  # заполняем значение по ключу
#     "Moscow": "Russia"  # заполняем значение по ключу
# }
# if question in countries:  # если переменная есть в dictionary
#     print(countries[question])  # выводим значение,введённое юзером
# else:  # в другом случае
#     print("Элемент не найден")  # пишем элемент не найден

# check_the_name = input("Введите имя: ")  # просим юзера ввести имя
# names = {  # создаём dictionary
#     "John": "Steven",  # заполняем значение по ключу
#     "Maga": "Zhabiev",  # заполняем значение по ключу
#     "Albert": "Einstein",  # заполняем значение по ключу
#     "Adolf": "Hitler"  # заполняем значение по ключу
# } # закрываем dictionary
# user = names.get(check_the_name, "Такого имени нет")  # get выводит значение,если такого элемента нет = print
# print(user)

# check_the_name = input("Введите имя: ")  # просим юзера ввести имя
# names_and_numbers = {  # создаём dictionary
#     "Maga": 380985638919,  # заполняем значение по ключу
#     "Sergey": 380985638914,  # заполняем значение по ключу
#     "Dima": 380995638916,  # заполняем значение по ключу
#     "Johan": 380985638910  # заполняем значение по ключу
# }  # закрываем dictionary
# print(names_and_numbers)
# if check_the_name in names_and_numbers:  # если данные, введённые юзером есть в dictionary
#     del names_and_numbers[check_the_name]  # удаляем ввёденные юзером ключ и значение
#     print(names_and_numbers)
# else:  # иначе
#     print("Такого имени нет")  # пишем такого имени нет

# check_the_lable = input("Введите имя: ")  # просим юзера ввести марку
# auto = {  # создаём dictionary
#     "BMW": "X5, X6, M5",  # заполняем значение по ключу
#     "Mercedes": "M1, M2, M3",  # заполняем значение по ключу
#     "Volkswagen": " P2, P1, PP",  # заполняем значение по ключу
#     "Mazda": "K1,K2,L3"  # заполняем значение по ключу
# }
# print(auto)
# finally_auto = auto.pop(check_the_lable, "Такого значения не существует")  # pop удаляет по значению ключа
# print(auto)
# print(finally_auto)
# auto.clear()  # очищаем полностью dictionary
# print(auto)


# users = {
#     "Serhii": "28",
#     "Maga": "22",
#     "Dima": "29"
# }
# print(users)
# users2 = users.copy()
# print(users2)

# cities = {
#     "Germany": "Berlin",
#     "Ukraine": "Kyiv",
# }
# cities2 = {
#     "Spain": "Madrid",
#     "Belarus": "Minsk"
# }
#
# cities.update(cities2)
# print(cities)
# print(cities2)

# user = {
#     "Maga": 380985638919,
#     "Johan": 38097827347,
#     "Riki": 343594589098,
#     "Olaf": 390242409024
# }
# for key in user:
#     print(key, user[key])
# for key in user.keys():
#     print(key)
# for value in user.values():
#     print(value)

# try:
#     check_the_user = input("Введите имя:")
#     check_the_information = input("Введите значение,которое хотите посмотреть: ID/Phone/Email")
#     users = {
#         "Maga": {
#             "ID": 1,
#             "Phone": 3982473284982,
#             "Email": "hdkajsdha@yahoo.com"
#         },
#         "Vasya": {
#             "ID": 2,
#             "Phone": 734234894,
#             "Email": "djsfhksdjhf@yahooo.com"
#         },
#         "Dima": {
#             "ID": 3,
#             "Phone": 3243249802394,
#             "Email": "skjgdjad@gmail.com"
#         }
#     }
#     print(users[check_the_user][check_the_information])
# except KeyError:
#     print("Неверные данные")
# finally:
#     print("Программа завершена")

# users = {
#     "Maga": {
#         "ID": 1,
#         "Phone": 3982473284982,
#         "Email": "hdkajsdha@yahoo.com"
#     },
#     "Vasya": {
#         "ID": 2,
#         "Phone": 734234894,
#         "Email": "djsfhksdjhf@yahooo.com"
#     },
#     "Dima": {
#         "ID": 3,
#         "Phone": 3243249802394,
#         "Email": "skjgdjad@gmail.com"
#     }
# }
#
#
# def user(info):
#     try:
#         check_the_user = input("Введите имя:")
#         check_the_information = input("Введите значение,которое хотите посмотреть: ID/Phone/Email")
#         print(info[check_the_user][check_the_information])
#     except KeyError:
#         print("Неверные данные")
#     finally:
#         print("Программа завершена")
#
#
# user(users)





