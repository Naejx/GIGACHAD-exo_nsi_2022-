# Créé par j.guerin1, le 13/10/2022 en Python 3.7
def entremele(liste1, liste2):
    a = []
    for i in range(len(liste1)):
        a.append(liste1[i])
        a.append(liste2[i])
    print(a)
    return a

assert entremele([1, 2, 3], [5, 6, 7]) == [1, 5, 2, 6, 3, 7], "/!\ entremele()"



def entremele2(liste1, liste2):
    a = []
    for i in range(len(liste1)):
        a.append(liste1[i])
        a.append(liste2[i])
    for i in range(len(liste2)):
        if liste1 > liste2:
            a.append(liste2[i])
    print(a)
    return a

assert entremele2([1, 2], [5, 6, 7, 8]) == [1, 5, 2, 6, 7, 8], "/!\ entremele2()"