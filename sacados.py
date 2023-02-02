# Créé par j.guerin1, le 26/01/2023 en Python 3.7
S = ((12, 4), (1, 2), (4, 10), (1, 1), (2, 2))

def SaD(S, M):
    assert type(S) == tuple and M > 0 and type(M) == int, '/!\ S doit être un tuple, et M un entier positif'
    X = [0, 0, 0, 0, 0]
    valeur = 0
    poids = M
    for i in range(len(S)):
        if S[i][0] < poids:
            valeur += S[i][1]
            poids -= S[i][0]
            X[i] = 1
    return valeur, "€, avec une masse restante de ", poids, 'kg, soit un poids de ', M-poids, 'kg', 'pour :', X



def selectdens(lst):
    lst_triee = []
    D = []
    for i in range(len(lst)):
        D.append(lst[i][1]/lst[i][0]*10)
    for i in range(len(D)):
        j = D.index(max(D))
        lst_triee.append(lst[j])
        D[j] = 0
    return lst_triee


def SaDens(S, M):
    assert type(S) == tuple and M > 0 and type(M) == int, '/!\ S doit être un tuple, et M un entier positif'
    X = [0, 0, 0, 0, 0]
    T = list(S)
    T = selectdens(T)
    valeur = 0
    poids = M
    for i in range(len(T)):
        if T[i][0] < poids:
            valeur += T[i][1]
            poids -= T[i][0]
            X[i] = 1
    return valeur, "€, avec un poids de ", M-poids, 'kg', 'pour :', X



print(SaD(S, 7))
print(SaDens(S, 15))




