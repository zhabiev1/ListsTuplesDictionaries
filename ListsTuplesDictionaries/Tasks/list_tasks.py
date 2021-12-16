question_2 = int(input("Cколько пользователей вы хотите записисать? "))
junior = []
middle = []
senior = []


def check_age():
    # question = int(input("Сколько Вам лет?"))
    counter = 0
    while question_2 > counter:
        question = int(input("Сколько Вам лет?"))
        counter += 1

        if question < 18:
            junior.append(question)
        elif 18 <= question < 21:
            middle.append(question)
        else:
            senior.append(question)


check_age()

print(junior)
print(middle)
print(senior)


info_junior = ["Преимущество: ", "Не нужно платить за проживание", "Лечите зубы за счёт родителей",
               "Ограничения: ", "нельзя долго гулять", " нельзя делать права"]
info_middle = ["Преимущество: ", "Помогают родители", "можно делать права",
               "Ограничения: ", "Нет денег", "Нужно поступать в универ"]
info_senior = ["Преимущество: ", "Можно работать", "Создавать бизнес",
               "Ограничения: ", "не помогают родителям", "Нужно работать"]


def junior_pros_and_cons(info):
    print("Если Вы Junior,то")
    for i in info:
        print(i)


def middle_pros_and_cons(info):
    print("Если Вы Middle, то")
    for i in info:
        print(i)


def senior_pros_and_cons(info):
    print("Если ВЫ Senior,то")
    for i in info:
        print(i)


junior_pros_and_cons(info_junior)
middle_pros_and_cons(info_middle)
senior_pros_and_cons(info_senior)




