import random as rd
import numpy as np

import liste_eleve
# Nombre minimal de personnes avant une boucle
# A réduire suivants le nombres de participant par classe
z = 3

# modifier les valeurs dans les range(n) avec le nombre de participant de la classe correspondante
MP = [(k,0) for k in range(8)]

HK = [(k,1) for k in range(33)]

KH = [(k,2) for k in range(20)]

PCSI = [(k,3) for k in range(46)]

MPSI = [(k,4) for k in range(47)]

ECS1= [(k,5) for k in range(40)]

PSI= [(k,6) for k in range(22)]

PC = [(k,7) for k in range(20)]
classe= ['MP','HK','KH','PCSI','MPSI','ECS1','PSI','PC']

def check(ordre, z):
    if isinstance(ordre, bool):
        return False
    l = len(ordre)
    res = [10 for k in range(8)]
    ordre = ordre + ordre[:8]
    minloc = [0 for k in range(8)]
    vu = [False for k in range(8)]
    for k in ordre:
        if vu[k]:
            # print(k, res[k], minloc[k])
            if minloc[k] < res[k]:
                # print('passe')
                res[k] = minloc[k]
            minloc[k] = 0
        else:
            vu[k] = True
        for i in range(8):
            if i != k:
                minloc[i] += 1
    # print(vu)
    for k in res:
        if k < z:
            return False
    else:
        return True, res

tocheck = True
while check(tocheck, z) == False:
    liste= MP+HK+KH+PCSI+MPSI+ECS1+PSI+PC
    premier = liste[rd.randint(0, len(liste)-1)]
    prob = np.array([z for k in range(8)])
    while len(liste)!=1 or (len(liste)==1 and (prob[liste[0][1]] <4 or liste[0][1] in [ordre[k][1][1] for k in range(4)])):
        ordre = []
        liste= MP+HK+KH+PCSI+MPSI+ECS1+PSI+PC
        
        prob = np.array([z for k in range(8)])
        
        premier = liste.pop(rd.randint(0, len(liste)-1))
        killer = premier
        while len(liste)>1:
            target = liste[rd.randint(0, len(liste)-1)]
            t = 0
            while prob[target[1]] <= z-1:
                target = liste[rd.randint(0, len(liste)-1)]
                t = t+1
                if t > 1000:
                    break
            if t>1000:
                break
            liste.remove(target)
            prob = prob+1
            prob[target[1]] = 0
            ordre.append([prob, killer, target])
            killer = target
            
        # print(liste)
        tocheck = [k[1][1]for k in ordre]
        tocheck += [liste[0][1]]
# print("restant:{}\nordre:{}".format(liste, ordre))
# print([[k[1], k[2]] for k in ordre])


# print(liste)

res = check(tocheck,z)

for k in range(8):
    print('{}: {} joueurs avant bouclage'.format(classe[k], res[1][k]))
    
tableau = {'MP':liste_eleve.MP ,
            'HK':liste_eleve.HK ,
            'KH':liste_eleve.KH ,
            'PCSI':liste_eleve.PCSI ,
            'MPSI':liste_eleve.MPSI ,
            'ECS1':liste_eleve.ECS1 ,
            'ECS2':liste_eleve.ECS2 ,
            'PSI':liste_eleve.PSI ,
            'PC':liste_eleve.PC }

print("\n\n\n\nCarte du jeu !:\n")
for k in ordre+[[np.array([0]), ordre[-1][2], liste[0]]]+[[np.array([0]), liste[0], premier]]:
    print('joueur {} a pour cible {}'.format(tableau[classe[k[1][1]]][k[1][0]],
                                                tableau[classe[k[2][1]]][k[2][0]]))