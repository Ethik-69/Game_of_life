#!/usr/bin/env python3
import pixel
import numpy

largeur = 300
hauteur = 300
zoom = 2
plateau=[]
plateau0=[]
for i in range(0, 300):
    plateau.append([1]*300)
    plateau0.append([1]*300)

pixel.initialiser(largeur, hauteur, zoom)

def read(tab):
    ##############################################
    'lit l\'etat des cellules du tableau'
    ##############################################
    for i in range(0, 300):
        for j in range(0, 300):
            tab[i][j] = int(pixel.lire(i, j))
    return tab



def etat_suivant(tab):
    def alive(tab, i, j):
        ##############################################
        'renvoi le nb de voisin vivant'
        ##############################################
        vivante = 0
        if tab[i][j] == 0 :
            vivante -= 1
        for x in range(i-1, i+1):
            for y in range(j-1, j+1):
                if tab[x][y] == 0 :vivante += 1
        return vivante
    ##############################################
    'calcul l\'etat suivant'
    ##############################################
    tab2=[]
    for i in range(0, 300):
        tab2.append([1]*300)
    for i in range(0, 300):
        for j in range(0, 300):
            nb_vivante = alive(tab, i, j)
            if nb_vivante % 2 != 0:tab2[i][j] = 0
            else:tab2[i][j] = 1
    return tab2

def write(tab):
    ##############################################
    'change les pixels'
    ##############################################
    for i in range(0, 300):
        for j in range(0, 300):
            if int(pixel.lire(i, j)) != tab[i][j]:
                pixel.marquer(i, j, tab[i][j])
    pixel.afficher(0)

def main(tab):
    ##############################################
    'main'
    ##############################################
    tab2 = etat_suivant(tab)
    write(tab2)
    return tab2

pixel.marquer(25, 25, 0)
pixel.marquer(25, 26, 0)
pixel.marquer(25, 27, 0)
pixel.marquer(25, 28, 0)
pixel.marquer(25, 29, 0)
pixel.marquer(25, 30, 0)
pixel.marquer(26, 25, 0)
pixel.marquer(27, 25, 0)
pixel.marquer(28, 25, 0)
pixel.marquer(29, 25, 0)
pixel.marquer(30, 25, 0)



pixel.afficher(1)
l = 0

plateau = read(plateau0)
for l in range(0, 30000):
    plateau = main(plateau)

#pixel.lire() lire un pixel
#pixel.initialiser(largeur, hauteur, zoom) pose le tableau
#pixel.marquer(i, j, 0) change etat pixel 0 on 1 off
#pixel.afficher() affiche le(s) pixel ?