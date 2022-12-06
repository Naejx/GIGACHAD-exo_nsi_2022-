# Créé par j.guerin1, le 06/10/2022 en Python 3.7

'''fonctions pour faire le taff d'école diREKT'''


liste=[13, 16, 5, 12, 16, 20, 12, 8, 17, 17, 7, 18, 5, 16, 7, 8,
     15, 13, 11, 10, 15, 14, 17, 13, 19, 6, 14, 8, 16, 8, 10, 11, 19, 7, 5]



def moyenne():
    for i in range(len(liste)):
        assert 0<=liste[i]<=20, "les notes ne peuvent être négatives ou supérieures à 20"
    print(round(sum(liste)/len(liste), 2))


def maxinote():
    for i in range(len(liste)):
        assert 0<=liste[i]<=20, "les notes ne peuvent être négatives ou supérieures à 20"
    maxi = 0
    for i in range(len(liste)):
        if maxi < liste[i]:
            maxi = liste[i]
    print(maxi)


def mininote():
    for i in range(len(liste)):
        assert 0<=liste[i]<=20, "les notes ne peuvent être négatives ou supérieures à 20"
    mini = 20
    for i in range(len(liste)):
        if mini > liste[i]:
           mini = liste[i]
    print(mini)


def pourcendessousde8():
    for i in range(len(liste)):
        assert 0<=liste[i]<=20, "les notes ne peuvent être négatives ou supérieures à 20"
    a = 0
    for i in range(len(liste)):
        if 8 > liste[i] :
            a += 1
    pourcen = a / len(liste) * 100
    print(pourcen, "%")


def pourcendessude12():
    for i in range(len(liste)):
        assert 0<=liste[i]<=20, "les notes ne peuvent être négatives ou supérieures à 20"
    a = 0
    for i in range(len(liste)):
        if 12 < liste[i] :
            a += 1
    pourcen = a / len(liste) * 100
    print(pourcen, "%")


def pourcentre8et12():
    for i in range(len(liste)):
        assert 0<=liste[i]<=20, "les notes ne peuvent être négatives ou supérieures à 20"
    a = 0
    for i in range(len(liste)):
        if 7 < liste[i] < 13 :
            a += 1
    pourcen = a / len(liste) * 100
    print(pourcen, "%")
