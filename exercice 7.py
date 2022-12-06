# Créé par j.guerin1, le 11/10/2022 en Python 3.7
def moyenne_geom(liste):
    geom = 0
    prod = 1
    for i in range(len(liste)):
        prod = liste[i] * prod
    geom = prod ** (1/len(liste))
    geom = round(geom)
    print(geom)
    return(geom)





assert moyenne_geom([2, 4, 8]) == 4, "/!\ moyenne_geo"