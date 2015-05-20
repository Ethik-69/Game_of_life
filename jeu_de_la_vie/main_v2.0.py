#!/usr/bin/env python3
import pixel
import numpy

largeur = 50
hauteur = 50
zoom = 10

pixel.initialiser(largeur, hauteur, zoom)

def read(tab):
    ##############################################
    'lit l\'etat des cellules du tableau'
    ##############################################
    for i in range(0, 50):
        for j in range(0, 50):
            tab[i][j] = int(pixel.lire(i, j))
    return tab

def alive(tab, i, j):
    ##############################################
    'renvoi le nb de voisin vivant'
    ##############################################
    vivante = 0
    if tab[i][j] == 0 :
        vivante -= 1
    for x in range(i-1, i+1):
        for y in range(j-1, j+1):
            if tab[x][y] == 0 :
                vivante += 1
    return vivante

def etat_suivant(tab):
    ##############################################
    'calcul l\'etat suivant'
    ##############################################
    tab2=[]
    for i in range(0, 50):
        tab2.append([1]*50)
    for i in range(0, 50):
        for j in range(0, 50):
            nb_vivante = alive(tab, i, j)
            print(nb_vivante)
            if nb_vivante % 2 != 0:
                tab2[i][j] = 1
            else:
                tab2[i][j] = 0
    return tab2

def write(tab):
    ##############################################
    'change les pixels'
    ##############################################
    for i in range(0, 50):
        for j in range(0, 50):
                pixel.marquer(i, j, tab[i][j])
    pixel.afficher(1)

def main(tab):
    ##############################################
    'main'
    ##############################################
    print('main')
    tab2 = etat_suivant(tab)
    write(tab2)
    return tab2

plateau=[]
plateau0=[]
for i in range(0, 50):
    plateau.append([1]*50)
    plateau0.append([1]*50)

pixel.marquer(40, 10, 0)
pixel.marquer(41, 10, 0)
pixel.marquer(42, 10, 0)
pixel.marquer(6, 40, 0)
pixel.marquer(7, 40, 0)
pixel.marquer(8, 40, 0)

pixel.afficher(1)
l = 0

plateau = read(plateau0)
print(plateau)
for l in range(0, 10000):
    plateau = main(plateau)

#pixel.lire() lire un pixel
#pixel.initialiser(largeur, hauteur, zoom) pose le tableau
#pixel.marquer(i, j, 0) change etat pixel 0 on 1 off
#pixel.afficher() affiche le(s) pixel ?