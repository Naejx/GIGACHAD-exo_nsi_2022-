# graphique d'évolution des temps de calculs
from time import perf_counter
from random import randint
import matplotlib.pyplot as plt

lst1=[randint(10,100) for i in range (10)]

def tri_insert(lst):
    """ Tri par insertion, mettre la liste en paramètre"""
    for i in range(1, len(lst)):
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i = i - 1
    return lst

def tri_select2(lst):
    lst_triee=[]
    while len(lst)>0 :
        lst_triee.append(lst.pop(lst.index(min(lst))))
    return lst_triee

tps_insert = []             # axe y1
tps_select2 = []            # axe y2
taille = []                 # axe x

for i in range (200,1001,200):                                                          # boucle pour fabriquer les valeurs des axes :#   x de 200 à 5 000 par pas de 200
    taille.append(i)
    lst=[randint(10,10000) for j in range(i)]
    t_actuel = perf_counter()                                                           # mémorise le temps actuel en µs
    tri_insert(lst)                                                                     # lance la fonction de tri 'tri_select'
    tps_insert.append(round(1000*(perf_counter()-t_actuel),0))
    t_actuel = perf_counter()
    tri_select2(lst)
    tps_select2.append(round(1000*(perf_counter()-t_actuel),0))

plt.clf()                                                                               ##  supprime les tracés précédents
plt.xlabel('évolution des performences')                                                ##  ajoute le nom de l'axe x
plt.plot(taille, tps_insert, color = 'g', linewidth=1, label = 'courbe insertion')        ##  trace l'axe y1 (liste axe x, liste axe y1, style de ligne, nom du tracé, couleur)
plt.plot(taille, tps_select2, color = 'b', linewidth=1, label = 'courbe select2')     ##  trace l'axe y2 (liste axe x, liste axe y2, style de ligne, nom du tracé, couleur)
plt.title('Comparation des perfs')                                                      ##  ajoute un titre au graphique
plt.legend()                                                                            ##  ajoute les légendes
plt.show()                                                                              ##  affiche le graphique







