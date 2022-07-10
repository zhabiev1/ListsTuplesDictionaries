# from math import sqrt
#
#
# a = int(input("Введите число а: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
#
# p = (a + b + c) / 2
# s = sqrt(p * (p-a) * (p-b) * (p-c))
#
# print(s)


# a = int(input("Введите число: "))
# if -15 < a <= 12 or 14 < a < 17 or a >= 19:
#     print(True)
# else:
#     print(False)


# a = int(input("Give the number a"))
# b = int(input("Give the number b"))
# c = int(input("Give the number c"))
#
# m = [a, b, c]
# m.sort()
# print(m[2])
# print(m[0])
# print(m[1])


finally_result = 0
pow_result = 0

while True:
    numbers = int(input("Give the numbers: "))
    finally_result += numbers
    pow_result += pow(numbers, 2)
    if finally_result == 0:
        print("сумма равна нулю")
        break

print(pow_result)







