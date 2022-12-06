# Créé par j.guerin1, le 20/10/2022 en Python 3.7

lst=[13, 16, 5, 12, 16, 20, 12, 8, 17, 17, 7, 18, 5, 16, 7, 8, 15, 13, 11, 10, 15, 14, 17, 13, 19, 6, 14, 8, 16, 8, 10, 11, 19, 7, 5]

def ekoldirekt(lst):
    print(round(sum(lst)/len(lst), 2))
    maxi = 0
    mini = 20
    a = 0
    b = 0
    c = 0
    for i in range(len(lst)):
        if maxi < lst[i]:
            maxi = lst[i]
        if mini > lst[i]:
           mini = lst[i]
        if 8 > lst[i] :
            a += 1
        pourcenA = a / len(lst) * 100
        if 12 < lst[i] :
            b += 1
        pourcenB = b / len(lst) * 100
        if 7 < lst[i] < 13 :
            c += 1
        pourcenC = c / len(lst) * 100
    print(maxi)
    print(mini)
    print(round(pourcenA), "%")
    print(round(pourcenB), "%")
    print(round(pourcenC), "%")


