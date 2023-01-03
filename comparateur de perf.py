# Créé par j.guerin1, le 13/12/2022 en Python 3.7
from time import perf_counter
from random import randint

lst=[randint(10,100000) for i in range(10000)]

def tri_select2(lst):
    lst_triee = []
    for i in range(len(lst)):
        lst_triee.append(lst.pop(lst.index(min(lst))))
    return lst_triee

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

d = perf_counter()
x = tri_select(lst)
##print("temps tri_select", round((perf_counter()-d),2),"s")

d = perf_counter()
x = tri_select2(lst)
##print("temps tri_se2", round((perf_counter()-d),2),"s")


def tri_insert(lst):
    """ Tri par insertion, mettre la liste en paramètre"""
    for i in range(1, len(lst)):
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i = i - 1
    return lst

tps_insert = []
for i in (10, 100, 1000, 10000):
    lst = [randint(1, i) for j in range(i)]
    d = perf_counter()
    tri_insert(lst)
    tps_insert.append((i, round((perf_counter()-d)*10**6, 0)))
print(tps_insert)


