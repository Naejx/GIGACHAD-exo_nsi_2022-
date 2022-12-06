# Créé par j.guerin1, le 17/11/2022 en Python 3.7

capitales ={"France":"Paris", "Allemagne":"Berlin", "Italie":"Rome", "Espagne":"Madrid", "Irlande":"Dublin", "Portugal":"Lisbonne", "Belgique":"Bruxelles", "Luxembourg":"Luxembourg", "Pays-Bas":"Amsterdam"}

def pays(ville, capitales):
    for i in capitales:
        if capitales[i] == ville :
            print(i)
            return i
    print(None)
    return None

pays("Paris", capitales)