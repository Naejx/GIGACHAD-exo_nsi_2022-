# Créé par j.guerin1, le 11/10/2022 en Python 3.7

def moyenne(liste):
    print(sum(liste)/len(liste))
    return sum(liste)/len(liste)
assert moyenne([3, 5, -9, 2, 4]) == 1, "/!\ moyenne()"