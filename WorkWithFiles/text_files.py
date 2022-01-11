# with open("hello.txt", "w") as file:  # открываем файл  и пер
#     file.write("Hello,World")
#
# with open("hello.txt", "a") as file:
#     file.write("\nGoodbye,World")
#
# with open("hello.txt", "a") as sentence:
#     print("\nI know what u did !", file=sentence)
#
# with open("hello.txt", "r") as file:
#      str1 = file.readline()
#      print(str1)
#      str2 = file.read()
#      print(str2)
#     str3 = file.readlines()
#     print(str3)

NAME_OF_PROJECT = "messages.txt"
message = list()
counter = int(input("сколько строк вы хотите ввести : "))

for i in range(counter):
    mes = input("Введит строку " + str(i + 1) + ": ")
    message.append(mes + "\n")

with open(NAME_OF_PROJECT, "w") as file:
    for i in message:
        file.write(i)

print("Считывание сообщения: ")
with open(NAME_OF_PROJECT, "r") as file:
    for i in file:
        print(i, end="")
