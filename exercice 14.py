# Créé par j.guerin1, le 17/11/2022 en Python 3.7
personnes ={"Jean Aymar":{"taille":178,"pays":"USA","age":31},"Clio Patre":{"pays":"Portugal","age":32,"taille":179}}


def son_age(nom,personnes):
    if nom in personnes :
        print(personnes[nom]["age"])
        return personnes[nom]["age"]
    else :
        print(None)
        return None

def taille_moy(personnes):
    som = 0
    for i in personnes :
        som += personnes[i]["taille"]
    print(round(som/len(personnes),1))
    return round(som/len(personnes),1)

son_age("Jean Aymar", personnes)
taille_moy(personnes)

