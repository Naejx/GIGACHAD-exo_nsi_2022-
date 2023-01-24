score = {'joueur_1': [0, 0], 'joueur_2': [0, 0], 'joueur_3': [0, 0]}

def molkky(score):
    victoire = False
    while victoire == False:
        for i in score:
            if score[i][0] < 50:
                test0 = entree()
                score[i][0] += test0
                print("Le nouveau score de ", i,"est ", score[i][0])
                if test0 == 0:
                    score[i][1] += 1
                elif test0 > 0:
                    score[i][1] = 0
            if score[i][0] > 50:
                score[i][0] = 25
            if score[i][0] == 50:
                victoire = True
                print("Le ", i," a gagné !")
                break
            if score[i][1] == 3:
                print("Le ", i," est éliminé")
                del score[i]

def entree():
    while True:
        score = input("Entrez votre score ")
        if score in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            return int(score)
        print("Score invalide, (doit se situer entre 0 et 12 inclus)")
molkky(score)