# Créé par j.guerin1, le 11/10/2022 en Python 3.7

def moy_pond(note, coef):
    pond = 0
    divi = 0
    for i in range(len(note)):
        pond = note[i] * coef[i] + pond
        divi = divi + coef[i]
    print(pond/divi)
    return(pond/divi)

assert moy_pond([10, 16, 5], [1, 0.5, 2]) == 8.0, "/!\ moy_pond()"