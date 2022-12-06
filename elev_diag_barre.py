# MP Affiche un diagramme sous forme de barres de #

def ajoute_espaces(mot, longueur):
    a = longueur - len(mot)
    if a > 0:
        for i in range(a):
            mot = mot + " "
    return mot

# TESTS
assert ajoute_espaces('Anne', 7) == 'Anne   '
assert ajoute_espaces('Luc', 7) == 'Luc    '
assert ajoute_espaces('nsi', 3) == 'nsi'
assert ajoute_espaces('', 2) == '  '

def taille_max(categories):
    a = 0
    for i in range(len(categories)):
        if a < len(categories[i]):
            a = len(categories[i])
    return a

#TESTS
assert taille_max(['Anne', 'Luc', 'Patrick', 'Sam']) == 7
assert taille_max(['tri', 'boucle', 'test', 'fonction']) == 8
assert taille_max(['isotopes','mercure','ballerines','covalence']) == 10

def barres(categories, valeurs):
    diagramme = ""
    for i in range(len(categories)):
        diagramme += ajoute_espaces(categories[i], taille_max(categories))
        diagramme += ' : '
        diagramme += '#'*valeurs[i]
        diagramme += '\n'
    return diagramme

#TESTS
categories=['Anne', 'Luc', 'Patrick', 'Sam']
valeurs = [10, 8, 5, 15]
diagramme = "Anne    : ##########\nLuc     : ########\nPatrick : #####\nSam     : ###############\n"
assert barres(categories, valeurs) == diagramme
categories = ['A', 'B', '', "EEEEE"]
valeurs = [1, 1, 0, 5]
diagramme = "A     : #\nB     : #\n      : \nEEEEE : #####\n"
assert barres(categories, valeurs) == diagramme
