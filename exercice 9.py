# Créé par j.guerin1, le 13/10/2022 en Python 3.7
def occurences(liste, valeur):
    ocu = 0
    ocu = liste.count(valeur)
    print(ocu)
    return ocu


assert occurences([3, 5, -9, 5, 4], 5) == 2, "/!\ occurences()"
assert occurences([3, 5, -9, 5, 4], 1) == 0, "/!\ occurences()"