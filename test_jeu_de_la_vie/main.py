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
            tab[i, j] = int(pixel.lire(i, j))
    return tab


def alive(tab, i, j):
    ##############################################
    'renvoi le nb de voisin vivant'
    ##############################################
    vivante = 0
    if tab[i, j] == 0 :
        vivante -= 1
    i = i - 1
    j = j + 1
    for x in range(i, j):
        for y in range(i, j):
            if tab[x, y] == 0 :
                vivante += 1
    return vivante


def etat_suivant(tab):
    ##############################################
    'calcul l\'etat suivant'
    ##############################################
    tab2 = numpy.zeros((50, 50), dtype=numpy.uint32)
    for i in range(0, 50):
        for j in range(0, 50):
            nb_vivante = alive(tab, i, j)
            if nb_vivante == 2:
                tab2[i, j] = 0
            elif nb_vivante == 3:
                tab2[i, j] = 0
            elif nb_vivante > 3:
                tab2[i, j] = 1
            elif tab[i, j] == 1 and nb_vivante == 3:
                tab2[i, j] = 0
    return tab2


def write(tab):
    ##############################################
    'change les pixels'
    ##############################################
    for i in range(0, 50):
        for j in range(0, 50):
            if tab[i, j] == 0:
                pixel.marquer(i, j, 0)
            else:
                pixel.marquer(i, j, 1)
    pixel.afficher(1)

def main(tab):
    ##############################################
    'main'
    ##############################################
    print('main')
    tab2 = etat_suivant(tab)
    write(tab2)
    return tab2


plateau0 = numpy.zeros((50, 50), dtype=numpy.uint32)
plateau = numpy.zeros((50, 50), dtype=numpy.uint32)
for i in range(0, 50):
    for j in range(0, 50):
        plateau0[i,j]=plateau[i,j]=1


pixel.marquer(2, 2, 0)

pixel.afficher(1)
l = 0

plateau = read(plateau0)

for l in range(0, 100):
    print(plateau)
    plateau = main(plateau)




input()


#pixel.lire() lire un pixel
#pixel.initialiser(largeur, hauteur, zoom) pose le tableau
#pixel.marquer(i, j, 0) change etat pixel 0 on 1 off
#pixel.afficher() affiche le(s) pixel ?