# NAEJ CONTENT
# -*- coding UTF-8 -*-
# Mini projet sur les dictionnaires Premiere Spe NSI
import string

texte0 = open("Extrait_de_la_Terre_a_la_Lune_JV.txt", "r")      #ouvre le fichier.txt
texte1 = texte0.read()                                          #converti en str
texte2 = texte1.lower()                                         #bascule les MAJ en min
texte0.close()

def barres(categories, valeurs):
    diagramme = ""
    for i in range(len(categories)):
        diagramme += categories[i]
        diagramme += ' : '
        diagramme += str(valeurs[i])
        diagramme += ' %'
        diagramme += '\n'
    return diagramme


def cpt_ltr(texte2):
    valeurs = []
    pourcen = []
    touslescarac = list(string.ascii_lowercase) + ['à']
    for i in range(len(touslescarac)):
        if touslescarac[i] in texte2:
            valeurs.append(texte2.count(touslescarac[i]))
    for i in range(len(valeurs)):
        pourcen.append(round(valeurs[i]/sum(valeurs)*100, 2))
    result = barres(touslescarac, pourcen)
    return result


print(cpt_ltr(texte2))