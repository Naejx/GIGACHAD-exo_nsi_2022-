# Créé par j.guerin1, le 15/11/2022 en Python 3.7
import random



def ODD(nmbdedes):
    '''
        Le paramètre nmbdedes défini le nombre de dés jetés par manches.

    '''
    PointA = 0
    PointB = 0
    A = []
    B = []
    C = 0
    D = 0
    PA = 0
    PB = 0
    OcuA = 0
    OcuB = 0
    gagnant = ""
    while PointA < 5 and PointB < 5:
        A = []
        B = []
        for i in range(nmbdedes):
            C = random.randint(1, 6)
            D = random.randint(1, 6)
            A.append(C)
            B.append(D)
        OcuA = A.count(6)
        OcuB = B.count(6)
        if OcuA >= 2:
            PointA += 1
        if OcuB >= 2:
            PointB += 1
        print("Alice:", A, "\nLe nombre de point(s) d'Alice est", PointA, "\nBob:",
    B,"\nLe nombre de point(s) de Bob est", PointB)
        if PointB > PointA:
            gagnant = "Bob"
        else:
            gagnant = "Alice"
    print("\nLe gagnant est", gagnant)

ODD(10)