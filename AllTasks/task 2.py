# x = float(input("Сколько спит часов спи Тимофей"))
# y = float(input("Cколько минут спит Тимофей в день"))
#
# print(x * 60 + y)
#

# a = float(input("сколько часов рекомендуется спать Ане?"))
# b = float(input("максимальное число сна"))
# h = float(input("Cколько часов спит Аня"))
#
# if h >= a and h <= b:
#     print("normal")
# elif h < a:
#     print("lack of sleep")
# elif h > b:
#     print("oversleep")
#

# rechner_1 = int(input("Введите первое число"))
# rechner_2 = int(input("Введите второе число"))
# operator = input("Введите операцию")

if operator == "+":
    print(rechner_1 + rechner_2)
elif rechner_2 == 0 and operator == "/":
    print("деление на ноль")
elif operator == "-":
    print(rechner_1 - rechner_2)
elif operator == "/":
    print(rechner_1 / rechner_2)
elif operator == "*":
    print(rechner_1 * rechner_2)
elif operator == "mod":
    print(rechner_1 % rechner_2)
elif operator == "pow":
    print(rechner_1 ** rechner_2)
elif operator == "div":
    print(rechner_1 // rechner_2)

# a = 1
# b = 2
#
# a,b = b,a
# print(a)
# print(b)