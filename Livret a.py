# Créé par j.guerin1, le 13/10/2022 en Python 3.7
def epargne():
    '''fonction permettant de calculer les interets annuels'''
    s = float(input("Entrez la somme initiale placée"))
    assert s>0, "n doit être positif"
    t = float(input("Entrez le taux d'interet du livret (valeur en %)"))
    assert t>0, "Le taux d'interet doit être positif (ne pas mettre le '%' à la fin)"
    a = int(input("Entrez le nombre d'années"))
    assert a>0,"le nombre d'années doit être positif"
    for i in range(a):
        STONKS = s * t / 100
        total = STONKS + s
    print(STONKS, '$ de bénéfice', "et vous avez", total, "€ sur votre épargne")
    return STONKS, '$ de bénéfice', "et vous avez", total, "€ sur votre épargne"