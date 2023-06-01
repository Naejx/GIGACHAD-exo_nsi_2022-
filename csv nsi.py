# Créé par j.guerin1, le 27/04/2023 en Python 3.7
import csv                                  # Importation du modul csv qui permet d'utiliser les fichiers csv
import matplotlib.pyplot as plt
##import numpy as np

entree = open("Rando_init.csv", "r")        # Ouvre le fichier csv dans une variable "entree"
rando = list(csv.reader(entree))            # Crée une variable pour stocker une liste des des données du fichier csv
entree.close()                              # Ferme le fichier csv dans la variable "entree"

##print(rando)                              # Affiche la liste "rando"

def crea_list(Rando):
    """renvoie une liste de listes de float  (alti, dist)
    sans les en-têtes, elle prend en argument la liste rando,
    liste de listes de str (couple (alti, dist)) avec en-têtes"""
    alti = []
    dist = []
    for i in range(1, len(Rando)):
        alti.append(Rando[i][0])
        dist.append(Rando[i][1])
    return (alti, dist)

##print(crea_list(rando))

def deniveles(alti):
    a = 0
    b = 0
    for i in range(len(alti)-1):
        calc = int(alti[i+1]) - int(alti[i])
        if calc >= 0:
            a += calc
        else:
            b += calc
    c = max(alti)
    return "le dénivelé positif est de ", a,"le dénivelé négatif est de ", b,"l'altitude max est de", c

##print(deniveles(crea_list(rando)[0]))

def cumul_distance(Distances):
    l = len(Distances)
    dist = 0
    distan = []
    for i in range(l):
        dist = round(float(dist) + float(Distances[i]), 2)
        distan.append(dist)
    return distan

##print(cumul_distance(crea_list(rando)[1]))


def profil_alti(alti, dist):
    plt.xlabel('distance en m')
    plt.ylabel('altitude en m')
    plt.plot(dist, alti)
    plt.show()

a = crea_list(rando)
alti = a[0]
dist = a[1]
distan = cumul_distance(crea_list(rando)[1])
profil_alti(alti, distan)
##profil_alti(crea_list(rando)[0], cumul_distance(crea_list(rando)[1]))
