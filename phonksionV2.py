# Créé par j.guerin1, le 29/09/2022 en Python 3.7
import math
import random
from tkinter import N

def devf(x):
    '''fonction permettant de calculer f(x) pour -1<=x<=1'''
    assert -1<=x<=1, "x n'est pas conforme"
    f = 1/1+x*x
    return f


def cercleinfo(r):
    '''fonction permettant de calculer le périmètre et le rayon d'un cerlce
     de rayon r'''
    assert r>0,             "r doit être positif"
    PERI = math.pi*2*r      #calcule le périmètre du cerlce
    SURF = math.pi*r**r     #calcule la surface du cerlce
    return PERI, SURF

def moyenne():
    '''calcule la moyenne sur 20 dans une liste de 35 notes'''
    LISTE = [random.randint(5,20) for i in range (35)]
    SOMMES = 0
    for i in range (35):
        SOMMES = SOMMES+LISTE[i]
    MOY = SOMMES/35
    return round(MOY)

def epargne(n):
    '''fonction permettant de calculer les interets annuels'''
    assert n>0, "n doit être positif"
    s = float(input("Entrez la somme initiale placée "))
    assert s>0, "la somme doit être positive"
    t = float(input("Entrez le taux d'interet du livret (valeur en %) "))
    assert t>0,"Le taux d'interet doit être positif (ne pas mettre le '%' à la fin)"
    STONKS = n*s*t/100
    return STONKS, '$ de bénéfice'