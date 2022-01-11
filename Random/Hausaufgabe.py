# import random
#
#
# def randomBoolean():
#     Rand = random.random()
#     print(Rand)
#
#     if Rand < 0.5:
#         return False
#     else:
#         return True
#
#
# print(randomBoolean())


# import random as rand
#
# WÜRFELANZAHL = 2
# WÜRFELSEITEN = 6
# WÜRFELVERSUCHE = 5000
#
# augensumme_anzahl = [0] * (WÜRFELANZAHL * WÜRFELSEITEN + 1)
#
# # Würfle alle versuche aus
# for _ in range(WÜRFELVERSUCHE):
#     augensumme = 0
#
#     # Bestimme die Summe aller geworfenen Würfel
#     for _ in range(WÜRFELANZAHL):
#         augensumme += rand.randint(1, WÜRFELSEITEN)
#     # Passe die gefundene anzahl an würfen an
#     augensumme_anzahl[augensumme] += 1
#
# # Gebe die Augensummen mit ihrem prozentuellen Anteil an vorgekommenen Würfen an
# a = 0
# b = 0
# for i in range(len(augensumme_anzahl)):
#     print(i, 100 * i / WÜRFELVERSUCHE)
#     if i % 2:
#         b += 100 * i / WÜRFELVERSUCHE
#     else:
#         a += 100 * i / WÜRFELVERSUCHE
#
# print(a)
# print(b)
# print("Es gibt keinen Sinn doppelte Ressoursen zu geben, weil der Unterschied nur ", a-b, "ist")


# import random as rand
# print("Gründe der Verspätung:")
#
#
# begrüßung = rand.choice(["Mein Zug hat sich verspätet", "Ich habe verschlafen", "ich habe mich verlaufen",
#                          "mein Auto war kaputt", "mein Wecker hat nicht funktioniert",
#                          "ich war in Berlin"])
#
# print(begrüßung + ".")
# print("Es tut mir wirklich leid.")