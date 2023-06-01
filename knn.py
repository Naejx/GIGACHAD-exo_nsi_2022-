# Créé par j.guerin1, le 16/05/2023 en Python 3.7
import pandas
import matplotlib.pyplot as plt
from math import *


iris = pandas.read_csv("iris.csv")
x = iris.loc[:,"longueur_petale"]
y = iris.loc[:,"largeur_petale"]
lab = iris.loc[:,"espece"]
liste = list(zip(x, y, lab))
echan = [float(input("x")), float(input("y")), None]


def dist_euclid(echan, liste):
    dist = []
    for i in range(len(liste)):
        distance = sqrt((liste[i][1] - int(echan[1]))**2 + (liste[i][0] - int(echan[0]))**2)
        dist += [[distance, liste[i][2]]]
    dist = sorted(dist)
    return dist


def dist2(dist):
    distrie = []
    for i in range(len(dist)):
        distrie.append(dist[i])
    return distrie


dist = dist2(dist_euclid(echan, liste))
k = 5


def KNN(dist, k):
    voisins = [[0,0],[1,0],[2,0]]
    couleur = ''
    for i in range(k):
        if dist[i][1] == 0:
            voisins[0][1] += 1
        elif dist[i][1] == 1:
            voisins[1][1] += 1
        elif dist[i][1] == 2:
            voisins[2][1] += 1
    maxi = 0
    for i in range(len(voisins)):
        if voisins[i][1] >= maxi:
            maxi = voisins[i][1]
            echan[2] = voisins[i][0]
    if echan[2] == 0:
        couleur = 'g'
        print('L espèce de la fleur est une setosa')
    elif echan[2] == 1:
        couleur = 'r'
        print('L espèce de la fleur est une versicolor')
    elif echan[2] == 2:
        couleur = 'b'
        print('L espèce de la fleur est une verginica')
    return couleur


couleur = KNN(dist, k)


plt.scatter(x[lab==0], y[lab==0], s=10, marker='^', color='g', label='setosa')
plt.scatter(x[lab==1], y[lab==1], s=10, marker='o', color='r', label='virginica')
plt.scatter(x[lab==2], y[lab==2], s=10, marker='.', color='b', label='versicolor')
plt.scatter(echan[0], echan[1], s=40, marker='X', color=couleur, label='exo')
plt.legend()
plt.show()