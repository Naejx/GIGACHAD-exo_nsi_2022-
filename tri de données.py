# Créé par j.guerin1, le 06/12/2022 en Python 3.7

lst = [2, 6, 8, 7, 9, 4, 3, 0, 1, 5]
lst2 = [2, 35, 38, 15, 50, 27, 100, 33]

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
    return lst



def tri_select2(lst):
    lst_triee = []
    for i in range(len(lst)):
        lst_triee.append(lst.pop(lst.index(min(lst))))
    return lst_triee

def tri_selectdécroissant(lst):
    lst_triee = []
    for i in range(len(lst)):
        lst_triee.append(lst.pop(lst.index(max(lst))))
    return lst_triee




print(tri_select(lst))
print(tri_select2(lst2))
print(tri_selectdécroissant(lst))
