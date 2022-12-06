# Créé par j.guerin1, le 13/10/2022 en Python 3.7

def decaladroite(liste):
    b = []
    for i in range(len(liste)):
        b.append(liste[i-1])
    print(b)
    return b

assert decaladroite([1, 2, 3]) == [3, 1, 2], "/!\ decaladroite"


def decalagauche(liste):
    b = []
    for i in range(len(liste)-1):
        b.append(liste[i+1])
    b.append(liste[0])
    print(b)
    return b

assert decalagauche([1, 2, 3]) == [2, 3, 1], "/!\ decaladroite"

