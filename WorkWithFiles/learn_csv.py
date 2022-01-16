import csv


NAME = "user.csv"

# users = [
#     ["Maga", 657675],
#     ["Dima", 456455],
#     ["Arina", 656576],
#     ["Natasha", 637745]
# ]
# with open(NAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
#  with open(NAME, "w", newline="") as file:
#      user = ["Maga", 22]
#      writer = csv.writer(file)
#     writer.writerow(user)

# with open (NAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     for i in reader:
#         print(i)

users = [
    {
        "Name": "Maga",
        "Age": 22
    },
    {
        "Name": "Dima",
        "Age": 25
    },
    {
        "Name": "Natasha",
        "Age": 24
    }
]

# with open(NAME, "w", newline="") as file:
#     info = ["Name", "Age"]
#     writer = csv.DictWriter(file, fieldnames=info)
#     writer.writeheader()
#     writer.writerows(users)

with open(NAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for i in reader:
        print(i)