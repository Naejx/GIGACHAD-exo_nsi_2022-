# Créé par j.guerin1, le 06/10/2022 en Python 3.7
def nmbdechiffre(): 
    '''écrire le nombre dans le parametre de la fonction'''
    a = input("uwu:")
    assert int(a) >= 0, 'le nombre doit être positif ou nul'
    print(len(a))

nmbdechiffre()