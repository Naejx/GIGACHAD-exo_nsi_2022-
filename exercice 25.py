# Créé par j.guerin1, le 17/11/2022 en Python 3.7
valeur_scrabble = {'kwxyz':10,'jq':8,'fhv':4, 'bcp':3, 'dmg':2,'aeilnorst':1}

## question A

def score(mot):
    points = 0
    for i in mot:
        for a in valeur_scrabble:
            if i in a :
                points += valeur_scrabble.get(a)
    print(points)
    return points

assert score("pizza") == 25, "/!\ score ne marche pas"
assert score("whisky") == 36, "/!\ score ne marche pas"
assert score("dedramatiser") == 15, "/!\ score ne marche pas"

## question B



