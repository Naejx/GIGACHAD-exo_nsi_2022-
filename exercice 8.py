# Créé par j.guerin1, le 13/10/2022 en Python 3.7
def contient_valeur(liste, valeur):
    for i in range(len(liste)):
        if valeur in liste:
            print(True)
            return True
        else:
            print(False)
            return False


assert contient_valeur([3, 5, 2], 5) == True, "/!\ contient_valeur()"
assert contient_valeur([3, 5, 2], 0) == False, "/!\ contient_valeur()"



def position_valeur(liste, valeur):
    a = 0
    if valeur in liste:
        a = liste.index(valeur)
        print(a)
    else:
        a = None
        print(a)
    return a


assert position_valeur([5, 3, 5], 5) == 0, "/!\ position_valeur"
assert position_valeur([5, 3, 5], 0) == None, "/!\ position_valeurde"



def positions_valeur(liste, valeur):
    a = []
    if valeur in liste:
        for i in range(len(liste)):
            if valeur == liste[i]:
                a.append(i)
    print(a)
    return a




assert positions_valeur([3, 5, 5], 5) == [1, 2], "/!\ positions_valeur()"
assert positions_valeur([3, 5, 5], 0) == [], "/!\ positions_valeur()"








