# Créé par j.guerin1, le 06/12/2022 en Python 3.7
def tri_select(lst):
    """ -> Fonction de tri de données, lst = les données à trier"""
    for i in range(len(lst)):
        mini = lst[i]
        index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < mini :
                mini = lst[j]
                index = j
                inter = lst[i]
        if lst[index] < lst[i]:
            lst[i] = lst[index]
            lst[index] = inter
    print(lst)
    return lst

tri_select([2, 6, 8, 7, 9, 4, 3, 0, 1, 5])